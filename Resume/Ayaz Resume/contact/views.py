from django.shortcuts import render
from django.core.mail import send_mail
from time import sleep
from django.contrib import messages
import smtplib
# Create your views here.

def Contact(request):
    context = {"contact":'active'}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']


        try: # error handling like i.e network error etc
            send_mail(
            subject,
            message,
            from_email = email,
            recipient_list = ['fa8031644@gmail.com'],
            fail_silently=False)
            messages.success(request,"Email Sent Successfully!")
        except:
            messages.success(request,"Email is not Sent!")
        sleep(1)
        

    return render(request,template_name='contact.html',context=context)





def Email_Sent(sender,name,subject,message):

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'fa8031644@gmail.com'
    # smtp_password = ''
    smtp_password = ''
    recipient = 'fa8031644@gmail.com'

    message = f"Subject: {subject} name {name}\n"+ message


    with smtplib.SMTP(host=smtp_server, port=smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password) 
        smtp.sendmail(sender, recipient, message)
