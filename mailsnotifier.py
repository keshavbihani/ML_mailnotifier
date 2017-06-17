import imaplib
import email

#making connection to gmail account
def getconnection():

    conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)

    gmail_user = 'XXXXX'

    gmail_pwd = 'XXXXXX'

    conn.login(gmail_user, gmail_pwd)

    conn.select()

    return conn

#get data of the latest mail on my mail-id
def getmailbody():

    conn=getconnection();

    result, data = conn.search(None, "ALL")

    ids = data[0]  # data is a list.

    id_list = ids.split()  # ids is a space separated string

    latest_email_id = id_list[-1]  # get the latest

    result, data = conn.fetch(latest_email_id, "(RFC822)")  # fetch the email body (RFC822) for the given ID

    raw_email = data[0][1]

    #print(raw_email)

    email_message = email.message_from_bytes(raw_email)

    subject = email_message['Subject']

    #print(subject)

    for part in email_message.walk():

            if part.get_content_type() == 'text/plain':

                email_content = part.get_payload()

    return [subject,email_content]
