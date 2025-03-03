def send_alert():
    print("🚨 ALERT! Suspicious object detected 🚨")
    # Code to send an email/SMS alert can be added here

def detect_threat(label):
    suspicious_objects = ["gun", "knife", "rifle", "explosive"]
    if label in suspicious_objects:
        send_alert()
