from unittest.mock import patch
from celery import shared_task
from django.test import TestCase
from .models import Applicant


@shared_task
def send_welcome_email(applicant_id):
    from .models import Applicant
    emp = Applicant.objects.get(id=applicant_id)
    print(f"[CELERY]Sending welcome email to {emp.email}")



class EmailTaskMockTest(TestCase):
    @patch("hrms.tasks.print") 
    def test_send_welcome_email_mocked(self, mock_print):
        emp = Applicant.objects.create(name="Bob", email="bob@example.com")
        send_welcome_email.delay(emp.id)
        mock_print.assert_called_once_with(f"[CELERY]Sending welcome email to {emp.email}")

