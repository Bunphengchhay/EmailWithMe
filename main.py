import smtplib, ssl
import config

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

def sendMail(server, sender, recipient):
    subject = 'Test subject'
    body = 'Hello World'
    msg = f'Subject: {subject}\n\n{body}'
    try:
        server.sendmail(sender, recipient, msg)
        print("Sucessfully sent")
    except Exception as e:
        print( e )

if __name__ == '__main__':

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
        'recipient' : config.recipient,
        'portnumber': 587
    }
    server = smtplib.SMTP(host = email_provider_dict[credential['email_provider']], port= credential['portnumber'])
    login(credential, server)
    sendMail(server, sender = credential['sender'], recipient= credential['recipient'])
    server.quit()