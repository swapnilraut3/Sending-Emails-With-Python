import os
import yagmail
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    recipients_list = ['recipient1@gmail.com', 'recipient2@gmail.com']
    subject = 'Hello, mail from Python email'
    body = 'Body of "Hello, mail from Python"'
    html = '''
    <html>
        <body>
             <p>Hi,<br>
                How are you? Doing Good?<br>
                <a href="http://www.realpython.com">Real Python</a> 
                has many great tutorials.
                </p>
        </body>
    </html>
    '''
    attachments_list = ['attachment.pdf', 'attachment.jpeg']

    user_name = os.environ.get('GMAIL_USR', None)
    if user_name == None:
        raise ValueError(
            'Gmail username is not set in enviornmental variable')

    password = os.environ.get('GMAIL_PWD', None)
    if password == None:
        raise ValueError(
            'Gmail Password is not set in enviornmental variable')

    # initiate the gmail SMTP connection
    mygmail = yagmail.SMTP(user=user_name, password=password)

    try:
        mygmail.send(to=recipients_list, subject=subject,
                     contents=[body, html], attachments=attachments_list)
    except Exception as e:
        print(e)
