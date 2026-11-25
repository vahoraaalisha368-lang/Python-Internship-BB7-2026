class Notification:
    def send(self):
        print("Sending generic notification...")

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification...")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification...")

notifications = [Notification(), EmailNotification(), SMSNotification()]

for n in notifications:
    n.send()