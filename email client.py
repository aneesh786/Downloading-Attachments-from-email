import imaplib
import base64
import email
import os

email_user = input('Email: ')
email_pass = input('Password: ')
mail = imaplib.IMAP4_SSL('mail.*****.com')
mail.login(email_user, email_pass)
mail.select('Inbox')
type, data = mail.search(None, '(SUBJECT "Web data high hitters")')
mail_ids = data[0]
id_list = mail_ids.split()
#print (id_list)


#(SUBJECT "Web data high hitters")

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('ISO-8859-1')
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet...
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('C:\Aneesh\Attachments', fileName)
            if not os.path.isfile(filePath):
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

