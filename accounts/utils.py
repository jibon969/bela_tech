import math, random
import requests
import json


# function to generate OTP
def generateOTP():
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""

    # length of password can be changed
    # by changing value in range
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


def sendSMS(msisdn, otp):
    try :

        url = 'https://smsplus.sslwireless.com/api/v3/send-sms'
        API_TOKEN = "egycwdhy-e2muyvdu-xwzchb02-nkrknigl-snlegvko"
        SID = "BELAFACENONAPI"
        msisdn = msisdn
        message_body = f"Your BELASEA verification code is {otp}. The code will expire in 6 hours. " \
                      f"Please do NOT share your OTP or PIN with others"
        csmsId = "4473433434684333392"

        headers = {
            'content-type': 'application/json'
        }

        payload = {
            "api_token": API_TOKEN,
            "sid": SID,
            "msisdn": msisdn,
            "sms": message_body,
            "csms_id": csmsId
        }
        response = requests.post(url, data=json.dumps(payload), headers=headers)

        context = {
            "status": True,
            "otp": otp,
            "sms_response": response.json()
        }

        return context

    except:
        context = {
            "status": False,
        }

        return context
