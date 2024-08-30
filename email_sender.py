import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# Load the HTML content from the file and create a Template object
html = Template(Path('index.html').read_text())

my_email = EmailMessage()
my_email['from'] = 'Viorica'
my_email['to'] = 'vioricaffoca@gmail.com'
my_email['subject'] = 'Hello Viorica, you will reach out it'

# Use the substitute method on the Template object
my_email.set_content(html.substitute({'name': 'Alina'}), subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('vioricaffoca@gmail.com', 'eydk hxjc cvma gzug')
    smtp.send_message(my_email)
    print('Email sent!')
