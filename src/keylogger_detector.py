from pynput import keyboard
import psutil

def detect_keylogger():
    print("🔍 Monitoring for suspicious keyboard activity... (Press ESC to stop)")

    def on_press(key):
        try:
            print(f"Key Pressed: {key.char}")
        except AttributeError:
            print(f"Special Key Pressed: {key}")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Check running processes for possible keyloggers
    suspicious_processes = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if "keylogger" in process.info['name'].lower():
            suspicious_processes.append((process.info['name'], process.info['pid']))

    if suspicious_processes:
        print("⚠️ Suspicious Keylogger Processes Detected!")
        for name, pid in suspicious_processes:
            print(f" - {name} (PID: {pid})")

    listener.join()

# Run detection
if __name__ == "__main__":
    detect_keylogger()
