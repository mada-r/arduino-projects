# Syncthing LCD Display

This project allows you to display the synchronization status of folders managed by Syncthing on an LCD display connected via serial communication.

## Requirements

Before running the application, ensure you have the following:

- Python 3.x installed on your machine.
- An LCD display connected to your computer via a serial port.
- Arduino IDE installed to upload the sketch to your Arduino board.

## Wiring Diagram

To connect the LCD display to your Arduino, use the following pin layout:

| LCD Pin | Arduino Pin | Description                |
|---------|-------------|----------------------------|
| RS      | 12          | Register Select             |
| E       | 11          | Enable                      |
| D4      | 5           | Data Pin 4                  |
| D5      | 4           | Data Pin 5                  |
| D6      | 3           | Data Pin 6                  |
| D7      | 2           | Data Pin 7                  |
| VSS     | GND         | Ground                     |
| VDD     | +5V         | Power                      |
| V0      | Potentiometer or Resistor | Contrast adjustment (optional; you can use a potentiometer for adjustable contrast or a fixed resistor) |

## Installation

1. **Download the project:**
   Clone the repository or download the ZIP file and extract it.

2. **Navigate to the project directory:**
   ```bash
   cd syncthing-lcd-display
   ```

3. **Install required packages:**
   You need to install the necessary Python packages. You can do this using pip:
   ```bash
   pip install requests pyserial
   ```

4. **Upload the Arduino Sketch:**
   - Open the `sketch.ino` file in the Arduino IDE.
   - Connect your Arduino board to your computer.
   - Select the correct board and port in the Arduino IDE.
   - Click on the upload button to send the sketch to the Arduino.

5. **Configuration:**
   Open `main.py` and update the following variables:
   - `SYNCTHING_URL`: Set this to the URL of your Syncthing instance (default is `http://<redacted>:8384`).
   - `API_KEY`: Replace `<redacted>` with your Syncthing API key.
   - `SERIAL_PORT`: Update this to match the serial port your LCD is connected to (e.g., `COM4` for Windows or `/dev/ttyUSB0` for Linux).
   - `BAUD_RATE`: Ensure this matches the baud rate set on your LCD display (default is `9600`).

## Usage

Run the application using the following command:

```bash
python main.py
```

The application will start and display the synchronization status of your Syncthing folders on the LCD screen.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
