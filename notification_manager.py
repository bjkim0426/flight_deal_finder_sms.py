from twilio.rest import Client

TWILIO_SID = ''
TWILIO_AUTH_TOKEN = ''
TWLIO_VIRTUAL_NUMBER = ''
TWLIO_VERTIFIED_NUMBER = ''

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWLIO_VIRTUAL_NUMBER,
            to=TWLIO_VERTIFIED_NUMBER
        )
        print(message.sid)