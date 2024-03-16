from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.urls import reverse


class EmailContent:
    def __init__(self, request, user, token) -> None:
        self.request = request
        self.user = user
        self.token = token

    def set_up_content(self):
        domain = get_current_site(self.request).domain
        verify_link = reverse('authentication:email_verify')
        absolute_url = f"http://{domain}{verify_link}?token={str(self.token)}"

        email_body = f"Hi {self.user.username}\nUse this link to verify your account: \n{absolute_url}"
        data = {
            'body': email_body, 'subject': 'Verify your email',
            'from_email': "customer_services@nawartravel.com", 'to': [self.user.email, ],
            }
        
        return data


class Email:
    @staticmethod
    def send_email(data) -> None:
        email = EmailMessage(**data)
        email.send()