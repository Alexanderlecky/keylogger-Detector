from src.process_scanner import scan_processes
from src.keylogger_detector import detect_keylogger
from src.monitor import start_monitoring
from src.ui import start_ui

import threading

def main():
    print("🚀 Starting Keylogger Detection Tool...")

    # Run process scanning
    scan_processes()

    # Start keylogger detection in a separate thread
    keylogger_thread = threading.Thread(target=detect_keylogger, daemon=True)
    keylogger_thread.start()

    # Start real-time monitoring
    monitoring_thread = threading.Thread(target=start_monitoring, daemon=True)
    monitoring_thread.start()

    # Start system tray UI
    start_ui()

if __name__ == "__main__":
    main()
