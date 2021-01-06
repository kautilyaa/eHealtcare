import os
from twilio.rest import Client
class message(object):
    def __init__(self):
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
    def sms(body,to):
        client = Client(account_sid, auth_token)
        message = client.messages \.create( body=body,from_='+91987654321', to=to )
        return(message.sid)#for logging we can have it returned
    def mms(body,url,to):  #url being an list of link like to different reports for medical examination
        client = Client(account_sid, auth_token)
        message = client.messages \.create( body=body,from_='+91987654321',media_url=url, to=to )
        return(message.sid)#for logging we can have it returned
