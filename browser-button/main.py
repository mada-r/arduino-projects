import serial
import subprocess

SERIAL_PORT = 'COM4' # replace with your serial port (if linux /dev/ttyUSB0)
BAUD_RATE = 9600 # replace with your baud rate

WEBSITE_URL = 'https://www.google.com/' # replace with your website

# you can change the browser to anything really just make sure you pass the correct path and that the browser is installed on your system
# and the flags
OPERA_GX_PATH = r'C:\Users\<username>\AppData\Local\Programs\Opera GX\opera.exe' # replace with your opera gx path

def open_opera_gx_private(url):
    subprocess.run([OPERA_GX_PATH, '--private', url]) # open website in private mode, if you want to open in normal mode, remove the --private flag

def listen_serial():
    try:
        # Open serial port
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            print(f"Listening on {SERIAL_PORT}...")
            
            while True:
                # Read data from serial port
                serial_data = ser.readline().decode('utf-8').strip()
                
                # Check if the message "BTN_PRESS" is received
                if serial_data == "BTN_PRESS":
                    print("Button pressed! Opening website in Opera GX private mode...")
                    try:
                        open_opera_gx_private(WEBSITE_URL)  # Open website in private mode
                    except Exception as e:
                        print(f"Error opening website: {e}")
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting program...")

if __name__ == "__main__":
    listen_serial()
