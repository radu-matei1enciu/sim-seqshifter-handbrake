# Sim-Sequential Shifter and Handbrake

An Arduino-based sequential shifter and handbrake controller for PC racing simulators. This project includes firmware for the Arduino and a Python script to ensure compatibility with simulators supporting standard gamepad input.

## Requirements

- **Hardware:**
  - Arduino board (e.g., Arduino Uno)
  - Sequential shifter mechanism
  - Handbrake mechanism
  - 3 Buttons, and 6 wires.

For the mechanism, get creative! Either use 3d printed pieces or whatever you can find around your house. This is what I did:
![image](https://github.com/user-attachments/assets/08c0e985-2675-4bed-846b-8a06467a9cf2)
In this setup, the wooden plates press the buttons when I pull or push the metal handles.

- **Software:**
  - [Arduino IDE](https://www.arduino.cc/en/software) for uploading firmware
  - Python 3.x installed on your PC
  - Required Python libraries: `pyserial`, `vgamepad`

## How to Set It Up

1. **Arduino Firmware:**
   - Open the `shifter.ino` file in the Arduino IDE.
   - Connect your Arduino board to the PC via USB.
   - Select the appropriate board and port in the Arduino IDE.
   - Upload the `shifter.ino` sketch to the Arduino.

2. **Python Script:**
   - Ensure Python 3.x is installed on your system.
   - Install the required Python libraries using pip:
     ```bash
     pip install pyserial vgamepad
     ```
   - Place the `shifter.py` script in your desired directory.
   - Use a text editor to modify "COM5" in the line of code below to the correct port in your case:
   - ser = serial.Serial('COM5', 115200, timeout=0.1)

3. **Hardware Connections:**
   - Connect the sequential shifter and handbrake mechanisms to the appropriate pins on the Arduino as defined in the `shifter.ino` code.
   - Downshift - pin 2,
   - Upshift - pin 3,
   - Handbrake - pin 4,
   - You are free to change these pins obviously 
   - Ensure all connections are secure and correctly mapped.

## How to Use It

1. **Running the Python Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `shifter.py`.
   - Execute the script:
     ```bash
     python shifter.py
     ```
   - The script will establish communication with the Arduino and translate inputs into gamepad signals.

2. **Integrating with Simulators:**
   - Launch your preferred racing simulator.
   - Configure the simulator's control settings to recognize the inputs from the sequential shifter and handbrake.
   - The device should be detected as a standard gamepad, allowing for straightforward mapping of controls.

**Note:** Ensure that the Python script is running in the background while using the simulator to maintain input translation.

---

For any issues or further assistance, please refer to the repository's [Issues](https://github.com/radu-matei1enciu/sim-seqshifter-handbrake/issues) section.
