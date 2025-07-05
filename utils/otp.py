from dotenv import load_dotenv
import requests
import os

load_dotenv()

BALE_OTP_URL = os.getenv("BALE_OTP_URL")
BALE_CLIENT_ID = os.getenv("BALE_CLIENT_ID")
BALE_CLIENT_SECRET = os.getenv("BALE_CLIENT_SECRET")


def normalize_phone_number(phone_number):
    phone_number = ''.join(filter(str.isdigit, phone_number))
    
    if phone_number.startswith('0'):
        phone_number = phone_number[1:]

    if len(phone_number) != 10:
        raise ValueError("شماره تلفن باید دقیقا 10 رقم باشد.")

    return "98" + phone_number


def get_token():
    url = f"{BALE_OTP_URL}/api/v2/auth/token"

    data = {
        "grant_type": "client_credentials",
        "client_id": BALE_CLIENT_ID,
        "client_secret": BALE_CLIENT_SECRET,
        "scope": "read"
    }

    response = requests.post(
        url=url,
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )

    if response.status_code == 200:
        return response.json()["access_token"]
    
    else:
        print(response.text)
        return None


def send_otp(phone_number, confirm_code):
    url = f"{BALE_OTP_URL}/api/v2/send_otp"

    access_token = get_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    data = {
        "phone": normalize_phone_number(phone_number),
        "otp": int(confirm_code)
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(
            "OTP sent successfully. Remaining balance:",
            response.json().get("balance")
        )

    else:
        print(
            "Error sending OTP:",
            response.status_code,
            response.text
        )
