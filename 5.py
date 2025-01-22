from abc import ABC, abstractmethod

# Абстракція для модуля повідомлень
class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Конкретний клас для надсилання повідомлень електронною поштою
class EmailSender(MessageSender):
    def send(self, message):
        print(f"Надсилання повідомлень електронною поштою: {message}")

# Конкретний клас для надсилання SMS
class SMSSender(MessageSender):
    def send(self, message):
        print(f"Надсилання SMS: {message}")

# Високорівневий модуль
class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

# Використання
email_sender = EmailSender()
sms_sender = SMSSender()

notification1 = Notification(email_sender)
notification1.notify("Це сповіщення електронною поштою")

notification2 = Notification(sms_sender)
notification2.notify("Це SMS-повідомлення")
