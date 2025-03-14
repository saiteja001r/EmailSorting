from src.utils.email_fetcher import fetch_emails
from src.utils.email_classifier import classify_email
from src.utils.email_mover import move_email_to_label
from config.config import EMAIL_FILE

# def main():
#     emails, mail = fetch_emails(limit=100)

#     with open(EMAIL_FILE, "r", encoding="utf-8") as file:
#         email_data = file.read()

#     email_entries = email_data.split("="*80)
#     for entry in email_entries:
#         if entry.strip():
#             lines = entry.split("\n")
#             email_id = lines[0].replace("Email ID: ", "").strip()
#             subject = lines[1].replace("Subject: ", "").strip()
#             body = "\n".join(lines[2:]).strip()

#             category = classify_email(body)
#             print(f"Subject: {subject}")
#             print(f"Category: {category}\n")
#             move_email_to_label(mail, email_id, category)

#     mail.logout()

# if __name__ == "__main__":
#     main()



# def main():
#     emails, mail = fetch_emails()

#     for email_data in emails:
#         category = classify_email(email_data["body"])
#         print(f"📩 Subject: {email_data['subject']}")
#         print(f"📂 Category: {category}\n")

#         # Move email to the corresponding label and mark as unread
#         move_email_to_label(mail, email_data["email_id"], category)

#     mail.logout()

# if __name__ == "__main__":
#     main()

def main():
    emails, mail = fetch_emails(limit=30)  # Fetch only 100 emails

    for email_data in emails:
        category = classify_email(email_data["body"])
        print(f"📩 Subject: {email_data['subject']}")
        print(f"📂 Category: {category}\n")

        # Move email to the corresponding label and mark as unread
        move_email_to_label(mail, email_data["email_id"], category)

    mail.logout()

if __name__ == "__main__":
    main()