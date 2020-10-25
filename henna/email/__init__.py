from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import threading

username = settings.EMAIL_HOST_USER


def send_email(name, recipient, subject, request, response):
    content = render_to_string('email.html', {'name': name, 'request': request, 'response': response})
    content = strip_tags(content)
    Email(subject, content, username, recipient).start()

class Email(threading.Thread):
    def __init__(self, subject, content, username, recipient):
        self.subject = subject
        self.recipient = (recipient,)
        self.content = content
        self.sender = username
        threading.Thread.__init__(self)

    def run(self):
        send_mail(self.subject, self.content, self.sender, self.recipient)
