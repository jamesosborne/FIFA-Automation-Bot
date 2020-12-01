import imaplib
import email


def authentication_code():
    user = ''
    password = ''
    imap_url = ''

    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(user, password)

    mail.select('inbox')

    result, data = mail.uid('search', None, 'ALL')

    inbox_item_list = data[0].split()

    most_recent = inbox_item_list[-1]

    result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')

    raw_email = email_data[0][1].decode("utf-8")

    email_message = email.message_from_string(raw_email)

    email_subject = email_message['Subject']

    code = email_subject[26:]

    return code




