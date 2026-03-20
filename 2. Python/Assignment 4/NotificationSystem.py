class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification...")
        print("Email Delivered")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification...")
        print("SMS Delivered")

def display_notifications(notification_list):
    count = 1
    for notification in notification_list:
        print(f"Notification {count}:")
        notification.send()
        count = count + 1

email_notification = EmailNotification()
sms_notification = SMSNotification()

notification1 = email_notification 
notification1.send()

notification2 = sms_notification
notification2.send()

notifications = [EmailNotification(), SMSNotification(), EmailNotification()]
display_notifications(notifications)