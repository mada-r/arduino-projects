import requests
import serial
import time

SYNCTHING_URL = 'http://<redacted>:8384'
API_KEY = '<redacted>'

SERIAL_PORT = 'COM4' # update with your serial port
BAUD_RATE = 9600 # Make sure the baud rate is the same as the arduinos


def get_folders(url, api_key):
    headers = {
        'X-API-Key': api_key
    }
    response = requests.get(f'{url}/rest/config/folders', headers=headers)
    response.raise_for_status()
    return response.json()

def get_sync_completion(url, api_key, folder_id=None):
    headers = {
        'X-API-Key': api_key
    }
    params = {'folder': folder_id} if folder_id else {}
    response = requests.get(f'{url}/rest/db/completion', headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def format_sync_completion(folder_name, completion_data):
    completion_percent = f"{completion_data['completion']:.2f}%"
    need_items = completion_data['needItems']
    
    folder_name = folder_name[:16]
    completion_percent = completion_percent[:16]
    
    line1 = folder_name
    line2 = completion_percent
    
    return line1, line2

def format_files_remaining(folder_name, completion_data):
    need_items = completion_data['needItems']
    folder_name = folder_name[:16]
    need_items_str = f"{need_items} Files".ljust(16)[:16]
    
    return folder_name, need_items_str

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)

        while True:
            time.sleep(2)

            try:
                folders = get_folders(SYNCTHING_URL, API_KEY)
                if not folders:
                    print("No folders found.")
                    return

                for folder in folders:
                    folder_id = folder['id']
                    folder_name = folder['label']

                    sync_completion = get_sync_completion(SYNCTHING_URL, API_KEY, folder_id)

                    # Only show folders with files syncing
                    if sync_completion['needItems'] > 0:
                        line1, line2 = format_sync_completion(folder_name, sync_completion)
                        ser.write(f"{line1.ljust(16)}{line2.ljust(16)}\n".encode())
                        time.sleep(5)

                        folder_name, need_items_str = format_files_remaining(folder_name, sync_completion)
                        ser.write(f"{folder_name.ljust(16)}{need_items_str.ljust(16)}\n".encode())
                        time.sleep(5)

            except requests.RequestException as e:
                print(f"Error fetching data from Syncthing: {e}")

    except serial.SerialException as e:
        print(f"Error with serial communication: {e}")
    finally:
        if ser.is_open:
            ser.close()

if __name__ == '__main__':
    main()
