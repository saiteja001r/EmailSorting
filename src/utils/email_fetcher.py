import imaplib
import email
from config.config import IMAP_SERVER, EMAIL_ACCOUNT, EMAIL_PASSWORD, EMAIL_FILE

# def fetch_emails(limit=100):
#     mail = imaplib.IMAP4_SSL(IMAP_SERVER)
#     mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
#     mail.select("inbox")

#     result, data = mail.search(None, "UNSEEN")
#     email_ids = data[0].split()
#     email_ids = email_ids[:limit]

#     emails = []
#     with open(EMAIL_FILE, "w", encoding="utf-8") as file:
#         for e_id in email_ids:
#             result, msg_data = mail.fetch(e_id, "(RFC822)")
#             raw_email = msg_data[0][1]
#             msg = email.message_from_bytes(raw_email)

#             subject = msg["subject"]
#             body = ""
#             if msg.is_multipart():
#                 for part in msg.walk():
#                     if part.get_content_type() == "text/plain":
#                         body += part.get_payload(decode=True).decode("utf-8", errors="ignore")
#             else:
#                 body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

#             emails.append({"email_id": e_id.decode('utf-8'), "subject": subject, "body": body})
#             file.write(f"Email ID: {e_id.decode('utf-8')}\n")
#             file.write(f"Subject: {subject}\n\n{body}\n")
#             file.write("="*80 + "\n")

#     return emails, mail



# def fetch_emails():
#     mail = imaplib.IMAP4_SSL(IMAP_SERVER)
#     mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
#     mail.select("inbox")

#     # Fetch unread emails
#     result, data = mail.search(None, "UNSEEN")
#     email_ids = data[0].split()

#     emails = []
#     for e_id in email_ids:
#         result, msg_data = mail.fetch(e_id, "(RFC822)")
#         raw_email = msg_data[0][1]
#         msg = email.message_from_bytes(raw_email)

#         subject = msg["subject"]
#         body = ""

#         # Extract email body
#         if msg.is_multipart():
#             for part in msg.walk():
#                 if part.get_content_type() == "text/plain":
#                     body += part.get_payload(decode=True).decode("utf-8", errors="ignore")
#         else:
#             body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

#         # Store email ID along with subject and body
#         emails.append({"email_id": e_id.decode('utf-8'), "subject": subject, "body": body})

#     return emails, mail



def fetch_emails(limit=10):
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ACCOUNT, EMAIL_PASSWORD)
    mail.select("inbox")

    # Fetch unread emails
    result, data = mail.search(None, "UNSEEN")
    email_ids = data[0].split()

    # Limit the number of emails to fetch
    email_ids = email_ids[:limit]

    emails = []
    for e_id in email_ids:
        result, msg_data = mail.fetch(e_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = msg["subject"]
        body = ""

        # Extract email body
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode("utf-8", errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

        # Store email ID along with subject and body
        emails.append({"email_id": e_id.decode('utf-8'), "subject": subject, "body": body})

    return emails, mail