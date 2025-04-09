import serial
import time
import vgamepad as vg

# Initialize virtual gamepad
gamepad = vg.VX360Gamepad()

# Configure the serial port
ser = serial.Serial('COM5', 115200, timeout=0.1)  # Match baud rate with Arduino

latest_data = ""  # Initialize to prevent crashes

while True:
    # Read only the most recent serial input
    while ser.in_waiting > 0:
        latest_data = ser.readline().decode('utf-8').strip()  # Read last available line

    if latest_data:  # Only process if data exists
        if latest_data == 'U':  # Upshift
            print("Upshift Pressed")
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()

        elif latest_data == 'u':
            print("Upshift Released")
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
            gamepad.update()
            
        elif latest_data == 'D':  # Downshift
            print("Downshift Pressed")
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        elif latest_data == 'd':
            print("Downshift Released")
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            gamepad.update()

        elif latest_data == 'H':
            print("Handbrake pulled")
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()

        elif latest_data == 'h':
            print("Handbrake released")
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            gamepad.update()
        # Reset latest_data after processing
        latest_data = ""
