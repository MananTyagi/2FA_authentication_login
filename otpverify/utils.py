# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('sid')
auth_token = os.environ.get('auth_token')
client = Client(account_sid, auth_token)
def send_sms(user_code, phone_number):
    message = client.messages.create(
                        body=f"{user_code}",
                        from_=os.environ.get('phone_number'),
                        to=f'{phone_number}'
                    )

    print(message.sid)
