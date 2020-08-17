import os
import yagmail

if __name__ == "__main__":
    recipients_list = ['recipient1@gmail.com', 'recipient2@gmail.com']
    subject = 'Hello, mail from Python email'
    contents = 'Body of "Hello, mail from Python"'
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
        mygmail.send(to=recipients, subject=subject,
                     contents=contents, attachments=attachments)
    except Exception as e:
        print(e)
