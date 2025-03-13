def move_email_to_label(mail, email_id, label):
    gmail_label = f'"[Gmail]/{label}"'
    result = mail.store(email_id, '+X-GM-LABELS', gmail_label)
    if result[0] == 'OK':
        print(f"Email {email_id} moved to {label}")
        mail.store(email_id, '-FLAGS', '\\Seen')
    else:
        print(f"Failed to move email {email_id} to {label}")
