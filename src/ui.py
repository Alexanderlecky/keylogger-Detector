from pystray import Icon, MenuItem, Menu
from PIL import Image
import sys
import plyer

def notify(title, message):
    plyer.notification.notify(
        title=title,
        message=message,
        app_name="Keylogger Detector",
        timeout=5
    )

def exit_app(icon, item):
    icon.stop()
    sys.exit()

def start_ui():
    icon_image = Image.open("assets/icon.png")

    menu = Menu(MenuItem("Exit", exit_app))
    icon = Icon("Keylogger Detector", icon_image, menu=menu)

    print("✅ System Tray UI running...")
    icon.run()

# def start_ui():
#     print("⚠️ Skipping System Tray UI due to missing support.")
#     return

