# Email with Python
## Introduction
#### This is a python program that will use SMTPLIB and python to send email. There are several functions in main.py that will demonstrate what kind of information we need in order to gain access to your email and as well as how to send email with Simple Mail Transfer Protocol (SMPT) to any recipients. For more information about SMTP please refer to smtplib documentation on https://docs.python.org/3/library/smtplib.html .

## Clone
    git clone git@github.com:Bunphengchhay/EmailWithMe.git

## Requirement
### The config in main.py is not being pushed onto github. Because it contains the credentials that are needed to send emails as the following. So make sure you have all your credential ready before working on this program.
    email_provider_dict = {
        'microsoft': 'smtp-mail.outlook.com',
        'gmail' : 'smtp.gmail.com',
        'yahoo': 'smtp.mail.yahoo.com',
        'icloud': 'smtp.mail.yahoo.com'
    }

    credential = {
        'email_provider' : 'gmail',
        'sender' : config.sender,
        'password' : config.password,
        'recipient' : config.recipient
    }
### You will need to go to your email account to generate a one time secure key to gain access from a third parties application to your email account. You need to log in to your account. Here is one of the example that you can generate key from your Google account: https://myaccount.google.com/u/1/security?pageId=none . Go to security then go to Signing in to Google and click on App passwords to generate the key that will be using as a password to login to your gmail account.

### NOTE: Different mail server will have different instruction to generate this key. Password in credential is not your password to your gmail account. email_provider is also different according to your mail server.
## Server
    server = smtplib.SMTP(host = email_provider_dict[credential['email_provider']], port= credential['portnumber'])
### This how how we initialize server using smtplib.
## Login
    def login(credential, server):
        sender =  credential['sender']
        password = credential['password']
        server.starttls()
        try:
            server.login(user = sender, password=password)
            print("Successfully login")
        except Exception as e:
            print("Unable to login")
            print(e)
### This function will take credential and server from the main function in order to send a request to login from your mail server. It will print the log if it is sucessfully login or else it will print the error.

## SendMail
    def sendMail(server, sender, recipient):
        subject = 'Test subject'
        body = 'Hello World'
        msg = f'Subject: {subject}\n\n{body}'
        try:
            server.sendmail(sender, recipient, msg)
            print("Sucessfully sent")
        except Exception as e:
            print( e )

### Similary, this sendMail function will take server, sender, and recipient from main.py in order to send email to your recipient. It will print the log if it is sucessfully login or else it will print the error.