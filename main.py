from datetime import datetime, date

from imap_tools import MailBox

GMAIL_EMAIL = 'example-test-dummy@gmail.com'  # Replace with your Gmail email address
GMAIL_APP_PASSWORD = ''  # Replace with your Gmail app password

# Create a MailBox object and login to the Gmail account
mailbox = MailBox('imap.gmail.com')
mailbox.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)

# Get the current date
from_date = datetime.strftime(date.today(), "%d-%b-%Y")  # Format: 04-Jul-2023

# Fetch emails from the specified date
filtered_emails = mailbox.fetch(criteria=f'ON {from_date}')

# Iterate over the filtered emails
for message in filtered_emails:
    # Extract email details
    receiver_email = message.to
    sender_email = message.from_
    subject = message.subject
    attachments = message.attachments
    email_date = message.date
    cc = message.cc
    bcc = message.bcc
    email_body = message.text
    email_headers = message.headers

    # Iterate over attachments, if any
    for attachment in message.attachments:
        filename = attachment.filename
        payload = attachment.payload
        # Process the attachment as needed

# Logout from the mailbox
mailbox.logout()