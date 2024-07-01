####DRAFT BELOW
#Click chrome
click(695, 2131)
time.sleep(3)
#Click chrome profile
click(1741, 2137)
time.sleep(3)
#Click workday bookmark
click(-3783, 145)
time.sleep(3)
#Click menu
click(-3760, 220)
time.sleep(3)
#Click time
click(-3634, 870)
time.sleep(3)
#Click check in
click(-2363, 1024)
time.sleep(3)
#Click ok
click(-1680, 1697)
time.sleep(3)

###Save screenshot to show successful clock in message
#Take screenshot
screenshot=pyautogui.screenshot()
#Save screenshot
screenshot.save('screenshot.png')

###Email screenshot
#Open gmail
click(-3648, 151)
#Click compose
click(-3628, 326)
#Type in email address
typewrite('wray.gabel@selu.edu')
time.sleep(1)
#Press tab (twice)
pyautogui.press('tab')
pyautogui.press('tab')
#Define current date (YYYY-MM-DD)
current_date=datetime.now().strftime('%Y-%m-%d') 
#Define text to type
text_to_type=f"Clock In Confirmation {current_date}"
#Write subject line
typewrite(text_to_type)
time.sleep(1)
#Click attachment
click(-1201, 2062)
#Click Desktop
click(-3697, 299)
#Click file search bar
click(-3536, 637)
#Type folder name
typewrite('AutoClockIn')
time.sleep(1)
#Press enter
pyautogui.press('enter')
#Type screenshot image name
typewrite('screenshot.png')
time.sleep(1)
#Press enter
pyautogui.press('enter')
#Press send
click(-1357, 2068)


###Email screenshot
#Open gmail
gmail_b=pyautogui.locateCenterOnScreen('LocateIcons/gmail.png')
click(gmail_b)
time.sleep(1)
#Compose email
compose_b=pyautogui.locateCenterOnScreen('LocateIcons/compose.png')
click(compose_b)
time.sleep(1)
#Type in email address
typewrite(email_ad)
time.sleep(1)
#Press tab (twice)
pyautogui.press('tab')
pyautogui.press('tab')
#Write subject line
typewrite('Clock In Confirmation {current_date}')
time.sleep(1)
#Attach screenshot
attach_b=pyautogui.locateCenterOnScreen('LocateIcons/attach.png')
click(attach_b)
time.sleep(1)

