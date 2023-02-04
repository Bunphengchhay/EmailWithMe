import smtplib, ssl
import config
# config contains the information for sender, recipient, and the app password

email_provider_dict = {
    'microsoft': 'smtp-mail.outlook.com',
    'gmail' : 'smtp.gmail.com',
    'yahoo': 'smtp.mail.yahoo.com',
    'icloud': 'smtp.mail.yahoo.com'
}

# email_provider = (input('which email do you want to use:')).lower()
# sender = input('Please enter your email address: ')
# password = input('Please enter your password: ')
# recipient = input('Your recipient email: ')

email_provider = 'gmail'
sender = config.sender
password = config.password
recipient = config.recipient

server = smtplib.SMTP(host = email_provider_dict[email_provider], 
                        port= 587)
server.starttls()
server.login(user = sender, password=password)


subject = 'Test subject2'
body = 'Hello World'
msg = f'Subject: {subject}\n\n{body}'

server.sendmail(sender, recipient, msg)
server.quit()
