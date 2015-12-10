from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string


def generic_email(user, this_from_email, this_subject, this_message):

    c = Context({
        'username': user.userprofile.get_display_name(),
        'subject': this_subject,
        'message': this_message,
    })

    email_subject = render_to_string('users/email/generic_message_subject.txt', c).replace('\n', '')
    email_txt_body = render_to_string('users/email/generic_message_body.txt', c)
    email_html_body = render_to_string('users/email/generic_message_body.html', c)

    subject, from_email, to = email_subject, this_from_email, user.email
    text_content = email_txt_body
    html_content = email_html_body

    email_headers = {
        "X-Mailgun-Campaign-Id": 'h0pk2',
        'Reply-To': this_from_email
    }

    msg = EmailMultiAlternatives(subject,
                                 text_content,
                                 from_email,
                                 [to],
                                 headers=email_headers
                                 )
    msg.attach_alternative(html_content, "text/html")

    return msg.send(fail_silently=False)
