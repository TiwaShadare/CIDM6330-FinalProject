from celery import shared_task
from unittest.mock import patch
from django.test import TestCase
from django.core.mail import send_mail
from hrms.models import Applicant



@shared_task
def send_welcome_email(applicant_id):
    from hrms.models import Applicant
    emp = Applicant.objects.get(id=applicant_id)
    print(f"[CELERY]Sending welcome email to {emp.email}")

@shared_task
def send_email_task(email, subject, message):
    send_mail(
        subject, 'Welcome to the team!',
        message, 'We are happy to have you on board. Please let us know if you have any questions.',
        [email], 'walter.white@yahoo.com',
    )


class EmailTaskMockTest(TestCase):
    @patch("hrms.tasks.print") 
    def test_send_welcome_email_mocked(self, mock_print):
        emp = Applicant.objects.create(name="Bob", email="bob@example.com")
        send_welcome_email.delay(emp.id)
        mock_print.assert_called_once_with(f"[CELERY]Sending welcome email to {emp.email}")



