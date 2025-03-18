import psutil

SUSPICIOUS_PROCESSES = ["keylog.exe", "hooker.exe", "logger.exe", "winhook.dll"]

def scan_processes():
    suspicious_found = []
    
    for process in psutil.process_iter(attrs=['pid', 'name']):
        process_name = process.info['name']
        process_id = process.info['pid']

        if process_name.lower() in SUSPICIOUS_PROCESSES:
            suspicious_found.append((process_name, process_id))

    if suspicious_found:
        print("⚠️ Suspicious Keylogger Processes Detected:")
        for name, pid in suspicious_found:
            print(f" - {name} (PID: {pid})")
    else:
        print("✅ No suspicious processes found.")
