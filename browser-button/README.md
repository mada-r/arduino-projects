# Browser Button

This project allows you to open a specified website in private mode using the Opera GX browser when a button press is detected via a serial connection.

## Requirements

Before running the application, ensure you have the following:

- Python 3.x installed on your machine.
- A serial device (e.g., Arduino) connected to your computer.
- Opera GX browser installed on your system.

## Installation

1. **Download the project:**
   Clone the repository or download the ZIP file and extract it.

2. **Navigate to the project directory:**
   ```bash
   cd browser-button
   ```

3. **Install required packages:**
   You need to install the necessary Python packages. You can do this using pip:
   ```bash
   pip install pyserial
   ```

4. **Configuration:**
   Open `main.py` and update the following variables:
   - `SERIAL_PORT`: Set this to the serial port your device is connected to (e.g., `COM4` for Windows or `/dev/ttyUSB0` for Linux).
   - `BAUD_RATE`: Ensure this matches the baud rate set on your serial device (default is `9600`).
   - `WEBSITE_URL`: Replace with the URL of the website you want to open.
   - `OPERA_GX_PATH`: Update this to the path of your Opera GX installation.

## Usage

Run the application using the following command:
```bash
python main.py
```

The application will listen for a button press on the specified serial port and open the website in Opera GX private mode when detected.
