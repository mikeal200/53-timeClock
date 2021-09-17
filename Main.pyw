import datetime
import time
from win10toast_click import ToastNotifier

running = True
toaster = ToastNotifier()

def stop():
    exit()
   
while running:
    today = datetime.datetime.now()
    day = today.strftime("%a")
    hour = int(today.strftime("%I"))
    minute = int(today.strftime("%M"))
    meridiem = today.strftime("%p")
    if(day == "Fri" and hour == 3 and minute in range(45, 59)):
        toaster.show_toast(
            title = "Submit your time sheet!!",
            msg = "Click to stop notifications!",
            icon_path = "icon/53.ico",
            duration = 5,
            threaded = False,
            callback_on_click = stop)
    time.sleep(20)
