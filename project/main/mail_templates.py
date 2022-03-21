from django.core.mail import send_mail, EmailMessage
from main.settings import admin_email, DEFAULT_FROM_EMAIL

def mail_activation_key(username, email, key):
    subject = 'Activation key'
    message = f"Hello {username} \n" \
              f'The following is an activation key for {email} \n' \
              f'You can copy the key and paste here: http://127.0.0.1:8000/account/activate \n' \
              f'Activation key:    {key}'
    send_mail(subject, message, from_email=None, fail_silently=True, recipient_list=[f'{email}'])


def validation_email_ping(username, user_email, attachment):
    subject = 'You have validation requests!'
    message = f'You have a validation request by:\n' \
              f'{username}\n' \
              f'{user_email}'
    mail = EmailMessage(subject, message, DEFAULT_FROM_EMAIL, [admin_email])
    mail.attach_file(attachment)
    mail.send()
