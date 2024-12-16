# Keylogger Project

## Overview
This project is part of the Computer and Network Security course (Lab 05). It involves the implementation of a keylogger program using Python, showcasing both the practical aspects of how such tools operate and their implications in cybersecurity.

## Keylogger Features
- Records all keyboard inputs, including alphanumeric and special keys.
- Logs are stored in a rotating log file (`key_log.txt`) with a maximum size of 5 MB and up to 3 backup files.
- Supports stopping the keylogger by pressing the `Escape` key.

### Key Components
1. **Logging Keyboard Inputs**:
   - Alphanumeric keys are logged with their corresponding character.
   - Special keys (e.g., `Space`, `Enter`, `Tab`) are identified and logged with descriptive names.

2. **Rotating Log File**:
   - Ensures efficient log file management by using Python's `RotatingFileHandler` from the `logging` module.

3. **User-Friendly Control**:
   - Press `Escape` to terminate the keylogger gracefully.

## Implementation
The keylogger is implemented using the `pynput` library for keyboard input capture. Below is an outline of its functionality:

1. **Key Press Logging**:
   - Alphanumeric keys are logged by their character.
   - Special keys are mapped to readable names using a predefined dictionary.

2. **Key Release Logging**:
   - Logs when keys are released.
   - Stops the listener when `Escape` is pressed.

3. **File Handling**:
   - Utilizes a rotating file handler to manage log files efficiently.

### Dependencies
- Python 3.x
- `pynput` library
- `logging` module (default Python library)

Install the required dependencies with:
```bash
pip install pynput
```

## Usage
1. Clone the repository or download the `keylogger.py` file.
2. Run the script:
   ```bash
   python keylogger.py
   ```
3. Logs will be saved in `key_log.txt`.
4. Press `Escape` to stop the keylogger.

## Ethical Considerations
This project is intended solely for educational purposes to understand the workings of keylogger software and its implications in cybersecurity. Unauthorized use of this software is strictly prohibited and may violate legal and ethical standards.

## Insights Gained
From this lab session:
1. Gained practical experience in developing a keylogger and understanding how attackers exploit such tools.
2. Understood the importance of secure coding practices and defensive mechanisms to mitigate keylogger threats.
3. Enhanced awareness of ethical responsibilities in cybersecurity.

## Disclaimer
This software should only be used for academic and educational purposes in controlled environments. The author is not responsible for any misuse of this program.
