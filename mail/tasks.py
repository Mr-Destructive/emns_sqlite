#from celery import shared_task

from time import sleep
from datetime import datetime    
from django.utils import timezone

#@shared_task
def sleepy(duration):
    sleep.delay(duration)
    return None

#@shared_task
def sendmails(request, reciever_email, message, send_time):
    port = 465
    password = request.user.gapps_key
    sender_email = request.user.email
    difference = (send_time - datetime.now(timezone.utc))
    total_seconds = difference.total_seconds()
    sleep(total_seconds)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, message)
    return None   

