from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from datetime import datetime    
from django.urls import reverse
# Create your models here.


class ScheduledMail(models.Model):
    sender = models.EmailField(max_length = 255) 
    subject = models.CharField(max_length = 78)
    body = models.CharField(max_length = 40000)
    send_on = models.DateTimeField(default = datetime.now,blank=True)
    recipients_list = models.CharField(max_length = 1023)

    attachment_file = models.FileField(blank=True, null=True, upload_to='mail/uploads/')


    def get_absolute_url(self):  
        return reverse('mail', args=(str(self.id),))


    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['-id', ]

    def tags_list(self):
        return self.recipients_list.split(',')
