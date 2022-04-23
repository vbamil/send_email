import smtplib
from email.message import EmailMessage
from string import Template

# Create a template that has placeholder value for name
email_content = Template('Hi $name, Learn AI & ML Programming from this channel')

email = EmailMessage()
email['from'] = 'Vinay AI Lab'
email['to'] = 'pythontutorial42@gmail.com'
email['subject'] = 'Please subscribe to my channel'

email.set_content(email_content.substitute({'name':'Ram'}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('vinayailab@gmail.com', 'subscribe')
    smtp.send_message(email)
    print('Email Sent!')
