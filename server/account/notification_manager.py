import os
import smtplib


EMAIL_FROM = os.environ.get("SMTP_EMAIL")
PASSWORD = os.environ.get("SMTP_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_msg(self, **kwargs):
        message = kwargs["message"]
        name = kwargs["name"]
        email = kwargs["email"]

        if EMAIL_FROM and PASSWORD:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()  # make secure connection
                connection.login(user=EMAIL_FROM, password=PASSWORD)
                connection.sendmail(
                    msg=f"Subject: {name} {email}\n\n{message}",
                    from_addr=EMAIL_FROM,
                    to_addrs="for.dev.in.mail@gmail.com",
                )
        else:
            print("SMTP credentials not defined.")
