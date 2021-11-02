from django.shortcuts import render
from .serializers import send_email_serializer
from rest_framework import viewsets
from .models import send_multi_email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Create your views here.

class send_email_view(viewsets.ModelViewSet):
    serializer_class = send_email_serializer
    queryset = send_multi_email.objects.all()


def sendsMultiMail(request):
    send_address = input('Enter Sender Email ')
    sender_pass = input('Enter Sender Password')
    list_of_send_address = input([])

    length = len(list_of_send_address)

    for i in range(length):
        x = list_of_send_address[i]
        receiver_mail = x

        print(receiver_mail)

        message = MIMEMultipart()
        message['From'] = send_address
        message['To'] = receiver_mail
        message['Subject'] = 'Mail using python'

        mail_content = input('Enter Your Message Here: ')

        message.attach(MIMEText(mail_content, 'plain'))

        filename = 'send_mails.py'

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            message.attach(part)

            smtp = s = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            s.login(send_address, sender_pass)
            text = message.as_string()
            smtp.sendmail(send_address, receiver_mail, text)
            s.quit()

            print('Mail Sent')


