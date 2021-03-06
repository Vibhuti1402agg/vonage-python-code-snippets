#Import dependencies
import vonage, os
from os.path import join, dirname
from dotenv import load_dotenv

#Load the environment
envpath = join(dirname(__file__),'../.env')
load_dotenv(envpath)

#Init the client
sms = vonage.Sms(
    key = os.getenv('VONAGE_API_KEY'),
    signature_secret = os.getenv('VONAGE_SIGNATURE_SECRET'),
    signature_method = 'md5'
)

#Define variables - replace FROM_NUMBER and TO_NUMBER with actual numbers
from_number = os.getenv('FROM_NUMBER')
to_number = os.getenv('TO_NUMBER')
text = 'A text message sent using the Nexmo SMS API'

#Sending the sms
response = sms.send_message({
    "from": from_number,
    "to": to_number,
    "text": text
})

if response["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {response['messages'][0]['error-text']}")
