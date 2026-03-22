# devnotifypy/notifier.py
import random
import string
import csv
import json
import platform
import psutil

# Firebase imports (optional)
try:
    import firebase_admin
    from firebase_admin import credentials, messaging
    _app_initialized = False
    _firebase_available = True
except ImportError:
    _firebase_available = False

# ================= Firebase Notifications =================
def init_firebase(json_path):
    if not _firebase_available:
        print("Firebase not installed. Skipping init.")
        return
    global _app_initialized
    if not _app_initialized:
        cred = credentials.Certificate(json_path)
        firebase_admin.initialize_app(cred)
        _app_initialized = True
        print("Firebase Initialized!")

def send_notification(title, message, token):
    if not _firebase_available:
        print("Firebase not installed. Skipping notification.")
        return
    msg = messaging.Message(
        notification=messaging.Notification(title=title, body=message),
        token=token
    )
    response = messaging.send(msg)
    print(f"Notification Sent! Response ID: {response}")

def random_activity_notification(token):
    if not _firebase_available:
        print("Firebase not installed. Skipping random notification.")
        return
    activities = [
        "liked your photo",
        "commented: Awesome!",
        "started following you"
    ]
    send_notification("Social App", random.choice(activities), token)

# ================= Developer Utilities =================
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def csv_to_json(csv_path, json_path):
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"CSV converted to JSON: {json_path}")

def system_info():
    info = {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "platform_version": platform.version(),
        "cpu_count": psutil.cpu_count(),
        "memory_total": psutil.virtual_memory().total
    }
    return info