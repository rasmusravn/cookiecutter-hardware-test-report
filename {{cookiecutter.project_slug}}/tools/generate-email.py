#!/usr/bin/env python3

"""
generate-email.py

A script to send an email update to the chosen recipient(s) from cookiecutter.
This is a generic SMTP example (not Gmail-specific).
"""

import argparse
import os
import smtplib
import ssl
from email.message import EmailMessage


def main():
    # ---------------------------------------------------------------------
    # 1. Customize your SMTP details
    # ---------------------------------------------------------------------
    SMTP_HOST = "mail.example.com"
    SMTP_PORT = 587  # or 25, 465, etc.
    SMTP_USER = "myapp@example.com"
    SMTP_PASSWORD = "YOUR_SMTP_PASSWORD"

    # ---------------------------------------------------------------------
    # 2. Define who the email is going to (from cookiecutter)
    #    Cookiecutter will replace {{ cookiecutter.intended_audience }}
    #    with whatever you typed during project generation.
    # ---------------------------------------------------------------------
    # If you expect multiple addresses, you could split by commas:
    # e.g. "team@company.com, manager@company.com"
    recipients_str = "{{ cookiecutter.emails_to }}"
    recipients_list = [r.strip() for r in recipients_str.split(",")]

    # ---------------------------------------------------------------------
    # 3. Parse optional command-line arguments for subject/body
    # ---------------------------------------------------------------------
    parser = argparse.ArgumentParser(
        description="Send a hardware test report update email."
    )
    parser.add_argument(
        "--subject",
        default="Hardware Test Report Update",
        help="Subject of the email (default: 'Hardware Test Report Update').",
    )
    parser.add_argument(
        "--body",
        default="Hello,\n\nThis is an automated update from the hardware test report tool.\n\nRegards,\nAutomation",
        help="Body text for the email.",
    )
    # If you want to attach a PDF or other file, add an argument here
    parser.add_argument(
        "--attachment",
        default="",  # default no attachment
        help="Path to an attachment file.",
    )
    args = parser.parse_args()

    # ---------------------------------------------------------------------
    # 4. Build the email message
    # ---------------------------------------------------------------------
    msg = EmailMessage()
    msg["From"] = SMTP_USER  # The 'From' address (your app)
    msg["To"] = ", ".join(recipients_list)
    msg["Subject"] = args.subject
    msg.set_content(args.body)

    # ---------------------------------------------------------------------
    # 5. Attach a file if requested
    # ---------------------------------------------------------------------
    if args.attachment:
        attachment_path = args.attachment
        if os.path.isfile(attachment_path):
            with open(attachment_path, "rb") as f:
                file_data = f.read()
            filename = os.path.basename(attachment_path)

            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=filename,
            )
            print(f"Attached file: {filename}")
        else:
            print(f"Attachment not found: {attachment_path}, skipping.")

    # ---------------------------------------------------------------------
    # 6. Send via a secured SMTP connection (STARTTLS)
    # ---------------------------------------------------------------------
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {str(e)}")


if __name__ == "__main__":
    main()
