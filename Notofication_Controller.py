from config import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

from_addr = SERVER_MAIL_ADDRES
my_pass = SERVER_MAIL_PASSWORD

def send_message(dest_addr, text):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = dest_addr
    msg['Subject'] = text.get('head')

    msg.attach(MIMEText(text.get('body'), 'html'))
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(from_addr, my_pass)
    text = msg.as_string()
    server.sendmail(from_addr, dest_addr, text)
    server.quit()   

def text_gen(key, username = None, race_id = None, race_date = None, race_new_date = None):
    match key:
        case "destination_soon":
            return {"head": DESTINATION_SOON.get('head'),
                    "body": DESTINATION_SOON.get('body') % (username, race_date)}
        case "home_soon":
            return {"head": HOME_SOON.get('head'),
                    "body": HOME_SOON.get('body') % (username, race_date)}
        case "trip_is_cancelled":
            return {"head": TRIP_IS_CANCELLED.get('head'),
                    "body": TRIP_IS_CANCELLED.get('body') % (username, race_date, race_id)}
        case "trip_reschedule":
            return {"head": TRIP_RESCHEDULE.get('head'),
                    "body": TRIP_RESCHEDULE.get('body') % (username, race_date, race_new_date, race_id)}
    return None

#send_message("npnbem.fm@gmail.com", text_gen("home_soon", username="maximka-Simka", race_date="01.04.2025"))