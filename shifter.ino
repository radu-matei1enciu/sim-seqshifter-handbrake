#define SHIFT_DOWN_PIN 2
#define SHIFT_UP_PIN 3
#define HANDBRAKE_PIN 4

bool is_handbrake_active = false;
bool is_shift_up_active = false;
bool is_shift_down_active = false;

const unsigned long DEBOUNCE_DELAY = 100;

struct Button {
  uint8_t pin;
  bool* state_ptr;
  const char* press_message;
  const char* release_message;
};

const Button buttons[] = {
  {SHIFT_DOWN_PIN, &is_shift_down_active, "D", "d"},
  {SHIFT_UP_PIN, &is_shift_up_active, "U", "u"},
  {HANDBRAKE_PIN, &is_handbrake_active, "H", "h"}
};
const uint8_t BUTTON_COUNT = sizeof(buttons) / sizeof(buttons[0]);

void handleButton(const Button& btn) {
  int current_state = digitalRead(btn.pin);
  
  if (current_state == LOW) {
    delay(DEBOUNCE_DELAY);
    
    if (digitalRead(btn.pin) == LOW) {
      if (*btn.state_ptr == false) {
        Serial.println(btn.press_message);
        *btn.state_ptr = true;
      }
      
      while (digitalRead(btn.pin) == LOW) {
        delay(10);
      }
    }
  } 
  else {
    if (*btn.state_ptr == true) {
      Serial.println(btn.release_message);
      *btn.state_ptr = false;
    }
  }
}

void setup() {
  Serial.begin(115200);
  
  for (uint8_t i = 0; i < BUTTON_COUNT; i++) {
    pinMode(buttons[i].pin, INPUT_PULLUP);
  }
}

void loop() {
  for (uint8_t i = 0; i < BUTTON_COUNT; i++) {
    handleButton(buttons[i]);
  }
  
  // delay(10);
}
