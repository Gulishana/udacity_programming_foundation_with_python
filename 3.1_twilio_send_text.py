from twilio.rest import Client
# from twilio import rest          # import the folder instead of the class

# 'rest' is a folder inside the folder 'twilio'
# 'Client' is a class inside the folder 'rest'
# for python2.7 is TwilioRestClient


print(twilio.version)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxx"        # account sid from www.twilio.com/try-twilio
auth_token = "faxxxxxxxxxxxxxxxxxxxxx"    # authorization token from www.twilio.com/try-twilio
client = Client(account_sid, auth_token)
# client = rest.Client(account_sid, auth_token)

# create an object/instance of class Client  =>  messsage
message = client.sms.message.create(
    body="Hello I'm Lisa",   # content of the text message
    to="+86XXXXXXXXXXX",     # your cellphone number
    from_="+86XXXXXXXXXXX"   # your Twilio phone number
)

print message.sid
