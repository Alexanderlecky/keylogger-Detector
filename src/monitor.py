import time
from src.process_scanner import scan_processes
from src.keylogger_detector import detect_keylogger
from src.ui import notify

def start_monitoring():
    print("🔄 Real-time Monitoring Started...")

    while True:
        scan_processes()
        notify("Security Alert", "Potential keylogger detected!")  # Trigger notification
        time.sleep(30)  # Check every 30 seconds
