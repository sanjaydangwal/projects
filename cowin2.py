import smtplib
from datetime import datetime, time
import time as tm
import requests

def create_session_info(center):
    return {"name": center["name"],
            "date": center["date"],
            "capacity": center["available_capacity"],
            "age_limit": center["min_age_limit"]}

def get_sessions(data):
    for centers in data["sessions"]:
        for center in centers:
            yield create_session_info(center)

def is_available(session):
    return session["capacity"] > 0

def is_eighteen_plus(session):
    return session["age_limit"] < 45

def get_for_seven_days(start_date):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
    params = {"pincode": 249201, "date": start_date.strftime("%d-%m-%Y")}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
    resp = requests.get(url, params=params, headers=headers)
    data = resp.json()
    # print(data)
    return [session for session in get_sessions(data) if is_eighteen_plus(session) and is_available(session)]

def create_output(session_info):
    return f"{session_info['date']} - {session_info['name']} ({session_info['capacity']})"

while True:
    # print(get_for_seven_days(datetime.today()))
    # print("Hello ")
    try:
        content = "\n".join([create_output(session_info) for session_info in get_for_seven_days(datetime.today())])
    except:
        content = []
        print('. ',end = "")

    if not content:
        # print("No availability ", end="")
        pass        
    else:
        from_address = "sanjay.dangwal199@gmail.com"
        to_address = "sanjay.dangwal199@gmail.com"
        email_msg = content

        with smtplib.SMTP(host='smtp.gmail.com', port='587') as server:
            server.ehlo()
            server.starttls()
            msg = "Subject: " + "Slot udate for Rishikesh" + '\n' + email_msg
            server.login(from_address, "**************")
            # server.send_message(email_msg, username, username)
            server.sendmail(from_address,to_address,msg)
    tm.sleep(20)