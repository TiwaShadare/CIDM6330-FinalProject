from django.test import TestCase
from hrms.models import Applicant
from django.test import TestCase
from hrms.tasks import send_welcome_email





class CeleryTaskTest(TestCase):
    def test_send_welcome_email_runs(self):
        emp = Applicant.objects.create(name="Alice", email="alice@example.com")
        result = send_welcome_email.delay(emp.id)
        self.assertTrue(result.successful())