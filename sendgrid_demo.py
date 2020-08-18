import os
import sendgrid
from sendgrid.helpers.mail import Mail, Content, Email, To
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    sg = sendgrid.SendGridAPIClient(
        api_key=os.environ.get('SENDGRID_API_KEY', None))
    from_email = Email("test@example.com")
    to_email = To("test@example.com")
    subject = "Sending with SendGrid is Fun"
    content = Content(
        "text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
