###Import
#Import modules
import pip
import pyautogui
import os
import time
import smtplib

#Import pyautogui functions
from pyautogui import click, displayMousePosition, typewrite
#Import datetime functions
from datetime import datetime
#Import mime functions
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

###Define
#Define email address to send confirmation email to (CHANGE MANUALLY FOR EACH PERSON)
email_ad='wray.gabel@selu.edu'
#Define app password (CHANGE MANUALLY FOR EACH PERSON)
pswd='eqrr itqb scnp alkj'
#Define current date (YYYY-MM-DD)
current_date=datetime.now().strftime('%Y-%m-%d') 
#Email ports/servers
smtp_port=587
smtp_server="smtp.gmail.com"

###Check in on Workday
#Open Chrome
chrome_b=pyautogui.locateCenterOnScreen('LocateIcons/chrome.png')
click(chrome_b)
time.sleep(1)
#Click chrome profile
click(1741, 2137)
time.sleep(1)
#Open workday
workday_b=pyautogui.locateCenterOnScreen('LocateIcons/workday.png')
click(workday_b)
time.sleep(1)
#Open menu
menu_b=pyautogui.locateCenterOnScreen('LocateIcons/menu.png')
click(menu_b)
time.sleep(1)
#Open time
time_b=pyautogui.locateCenterOnScreen('LocateIcons/time.png')
click(time_b)
time.sleep(1)
#Click check out
#checkout_b=pyautogui.locateCenterOnScreen('LocateIcons/checkout.png')
#click(checkout_b)
time.sleep(1)
#Click ok
ok_b=pyautogui.locateCenterOnScreen('LocateIcons/ok.png')
click(ok_b)
time.sleep(1)

###Save screenshot to show successful clock in message
#Take screenshot
screenshot=pyautogui.screenshot()
#Save screenshot
screenshot.save('screenshot.png')

###Email screenshot
#Write function for sending email with attachment
def send_emails(email_ad):
    body=f'Attached is a screenshot to confirm that you have been successfully clocked out. If this screenshot does not depict a success message for the current date ({current_date}), then you have not successfully been clocked out.'

    #Make a MIME object to define parts of the email
    msg=MIMEMultipart()
    msg['from']=email_ad
    msg['to']=email_ad
    msg['subject']=f'Confirmation of successful workday clock out on {current_date}.'
    #Attach body of message
    msg.attach(MIMEText(body, 'plan'))

    filename='screenshot.png'

    #Open the attachment in python as a binary
    attachment=open(filename, 'rb')

    #Encode as base 64
    attachment_package=MIMEBase('application', 'octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(attachment_package)

    #Cast as a string
    text=msg.as_string()

    #Connect to server
    print('Connecting to server...')
    TIE_server=smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_ad, pswd)
    print("Successfully connected to server.")
    print()

    #Send the email
    print()
    print(f'Sending email to - {email_ad}')
    TIE_server.sendmail(email_ad, email_ad, text)
    print(f"Email successfully sent to {email_ad}.")
    
    TIE_server.quit() 

send_emails(email_ad)    