# demo/test_library.py
from devnotifypy import (
    init_firebase,
    send_notification,
    random_activity_notification,
    generate_password,
    system_info,
    csv_to_json
)

print("=== Testing Developer Utilities ===")
print("Random password:", generate_password(12))
print("System info:", system_info())

# Optional CSV to JSON test (create data.csv to test)
# csv_to_json("data.csv", "data.json")

print("\n=== Testing Firebase Notifications ===")
# If you have a Firebase JSON and real device token, uncomment these lines:
# init_firebase("service_account.json")
# token = "YOUR_REAL_DEVICE_TOKEN"
# send_notification("Hello!", "This is a test notification", token)
# random_activity_notification(token)
print("Library tests complete!")