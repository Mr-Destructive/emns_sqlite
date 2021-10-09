from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .models import ScheduledMail
from .forms import MailForm

from django.core.mail import send_mail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime    
import smtplib, ssl
import time, os
import json

from django.utils import timezone
from mail.tasks import sendmails
# Create your views here.
def handle_uploaded_file(f):  
    with open('mail/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  

class AddMailView(LoginRequiredMixin, CreateView):
    model = ScheduledMail
    form_class = MailForm
    template_name = 'mail/add.html'
    
    def form_valid(self, form):
        form.instance.sender = self.request.user.email
        sendtime = form.instance.send_on
        
        port = 465
        sender_email = self.request.user.email
        reciever_email = form.instance.tags_list()
        password = self.request.user.gapps_key
        body = form.instance.body
        subject = form.instance.subject

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ','.join(reciever_email)
        message["Subject"] = subject
        
        message.attach(MIMEText(body, "plain"))
        
        file = form.instance.attachment_file
        if file:
            with open(file, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            message.attach(part)
            message.attach(file.name, file.read(), file.content_type)

        message = message.as_string()

        
        context = ssl.create_default_context()
        

        # instead of sending mails from here, we will call this later in the mails/tasks.py file to schedule
        # sendmails(self.request, reciever_email, message, sendtime)

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)

        return super(AddMailView, self).form_valid(form)




