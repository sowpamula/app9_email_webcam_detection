import smtplib
import imghdr
from email.message import EmailMessage


PASSWORD = "puspkltxpqzzthcn"
SENDER = "sowjanya25081996@gmail.com"
RECEIVER = "sowjanya25081996@gmail.com"


def send_email(image_path):
    print("Send email function started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_contet("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("Send email function ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")



