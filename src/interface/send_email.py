from django.core.mail import EmailMessage
from django.template import loader
from dance.settings import EMAIL_HOST_USER

import time


def send_html_mail(subject, content, recipient_list):
    html_content = loader.render_to_string(
                        'guest/email/email.html',
                        {
                            'email': content['email'],
                            'date': time.strftime("%Y.%m.%d", time.localtime()),
                            'manage_url': content['manage_url'],
                            'questionnaire_url': content['questionnaire_url'],
                        }
                   )
    try:
        msg = EmailMessage(subject, html_content, EMAIL_HOST_USER, recipient_list)
        msg.content_subtype = "html"
        msg.send()
    except:
        pass        