# Vault Keylogger

A minimal keylogger demo that records keystrokes to `vault_keylog.txt` for educational purposes. **Use only with explicit consent on systems you own or are authorized to test.**

## How it works
- Listens for key presses via `pynput.keyboard.Listener`.
- Logs alphanumeric keys directly; labels common special keys (space, enter, backspace).
- Writes buffered keystrokes to `vault_keylog.txt` every 10 seconds.

## Requirements
- Python 3.8+
- `pynput` (`pip install pynput`)

## Usage
```pwsh
cd "c:\Users\davix\Music\ATLAS\Internship project\Keylogger"
python vault_keylog.py
```
Press keys; logs accumulate in `vault_keylog.txt`.

## Notes
- Stop the script with Ctrl+C in the terminal.
- Running keyloggers without permission is illegal and unethical; obtain explicit consent and comply with local laws and organizational policies.
