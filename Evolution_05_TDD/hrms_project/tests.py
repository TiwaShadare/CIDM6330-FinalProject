from django.test import TestCase
from django.urls import reverse
from hrms.models import Applicant, Job, Application, Interview, Offer, Company 


# Create your tests here.


#Testing API for Applicant Creation.
class ApplicantAPITests(TestCase):
    def test_create_applicant(self):
        self.Applicant_data = {
             'first_name': 'Walter',
            'last_name': 'White',
            'phone_number': '310-555-5555',
            'email': 'walter.white@yahoo.com',
            'position': 'Developer',
            'salary': 100000
        }

        response = self.client.post(**self.Applicant_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['first_name'], 'Walter')
        self.assertEqual(response.data['last_name'], 'White')
        self.assertEqual(response.data['phone_number'], '310-555-5555')
        self.assertEqual(response.data['salary'], 100000)

#Testing API for Applicant update.
class ApplicantUpdateTests(TestCase):
    def test_update_applicant(self):
        self.Applicant_data = {
            'first_name': 'Bob',
            'last_name':'Dylan',
            'email':'bobd@gmail.com',
            'position':'Manager',
            'salary': 80000
        }

    def test_update_Applicant(self):
        self.Applicant.first_name = 'Bob'
        self.Applicant.save()
        updated_Applicant = Applicant.objects.get(id=self.Applicant.id)
        self.assertEqual(updated_Applicant.first_name, 'Bob')

#Testing Applicant Deletion.
class ApplicantDeleteTests(TestCase):
    def setUp(self):
        self.Applicant = Applicant.objects.create(
            first_name='Skylar',
            last_name='Jenkins',
            email='sjenkins@yahoo.com',
            position='HR',
            salary=50000
        )

    def test_delete_Applicant(self):
        Applicant_id = self.Applicant.id
        self.Applicant.delete()
        with self.assertRaises(Applicant.DoesNotExist):
            Applicant.objects.get(id=Applicant_id)


#Testing Job Creation.
class JobModelTests(TestCase):
    def setUp(self):
        self.job_data = {
            'title': 'Software Engineer',
            'location': 'Remote',
            'department': 'Engineering',
            'salary': 100000,
            'status': 'Open',
            'posting_date': '2025-10-01',
            'closing_date': '2025-12-01'
        }

    def test_create_job(self):
        job = Job.objects.create(**self.job_data)
        self.assertEqual(job.title, 'Software Engineer')
        self.assertEqual(job.location, 'Remote')
        self.assertEqual(job.department, 'Engineering')
        self.assertEqual(job.salary, 100000)
        self.assertEqual(job.status, 'Open')
        self.assertEqual(job.posting_date, '2025-10-01')
        self.assertEqual(job.closing_date, '2025-12-01')


#Testing Job update.
class JobUpdateTests(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            title='Data Scientist',
            location='New York',
            department='Data Science',
            salary=120000,
            status='Open',
            posting_date='2025-10-01',
            closing_date='2025-12-01'
        )

    def test_update_job(self):
        self.job.title = 'Senior Data Scientist'
        self.job.save()
        updated_job = Job.objects.get(id=self.job.id)
        self.assertEqual(updated_job.title, 'Senior Data Scientist')


#Testing Job Deletion.
class JobDeleteTests(TestCase):
    def setUp(self):
        self.job = Job.objects.create(
            title='Project Manager',
            location='San Francisco',
            department='Management',
            salary=110000,
            status='Open',
            posting_date='2025-10-01',
            closing_date='2025-12-01'
        )

    def test_delete_job(self):
        job_id = self.job.id
        self.job.delete()
        with self.assertRaises(Job.DoesNotExist):
            Job.objects.get(id=job_id)

#Testing Application Creation.
class ApplicationModelTests(TestCase):
    def setUp(self):
        self.application_data = {
            'job_id': 1,
            'application_date': '2025-10-01',
            'status': 'Pending'
        }

    def test_create_application(self):
        application = Application.objects.create(**self.application_data)
        self.assertEqual(application.job_id, 1)
        self.assertEqual(application.application_date, '2025-10-01')
        self.assertEqual(application.status, 'Pending')

#Testing Application update.
class ApplicationUpdateTests(TestCase):
    def setUp(self):
        self.application = Application.objects.create(
            job_id=1,
            application_date='2025-10-01',
            status='Pending'
        )

    def test_update_application(self):
        self.application.status = 'Accepted'
        self.application.save()
        updated_application = Application.objects.get(id=self.application.id)
        self.assertEqual(updated_application.status, 'Accepted')

#Testing Application Deletion.
class ApplicationDeleteTests(TestCase):
    def setUp(self):
        self.application = Application.objects.create(
            job_id=1,
            application_date='2025-10-01',
            status='Pending'
        )

    def test_delete_application(self):
        application_id = self.application.id
        self.application.delete()
        with self.assertRaises(Application.DoesNotExist):
            Application.objects.get(id=application_id)


#Testing Interview Creation.
class InterviewModelTests(TestCase):
    def setUp(self):
        self.interview_data = {
            'applicant_id': 1,
            'recruiter_id': 1,
            'interview_date': '2025-10-01',
            'interview_time': '10:00:00',
            'interview_status': 'Scheduled'
        }

    def test_create_interview(self):
        interview = Interview.objects.create(**self.interview_data)
        self.assertEqual(interview.applicant_id, 1)
        self.assertEqual(interview.recruiter_id, 1)
        self.assertEqual(interview.interview_date, '2025-10-01')
        self.assertEqual(interview.interview_time, '10:00:00')
        self.assertEqual(interview.interview_status, 'Scheduled')

#Testing Interview update
class InterviewUpdateTests(TestCase):
    def setUp(self):
        self.interview = Interview.objects.create(
            applicant_id=1,
            recruiter_id=1,
            interview_date='2025-10-01',
            interview_time='10:00:00',
            interview_status='Scheduled'
        )

    def test_update_interview(self):
        self.interview.interview_status = 'Completed'
        self.interview.save()
        updated_interview = Interview.objects.get(id=self.interview.id)
        self.assertEqual(updated_interview.interview_status, 'Completed')

#Testing Interview Deletion.
class InterviewDeleteTests(TestCase):
    def setUp(self):
        self.interview = Interview.objects.create(
            applicant_id=1,
            recruiter_id=1,
            interview_date='2025-10-01',
            interview_time='10:00:00',
            interview_status='Scheduled'
        )

    def test_delete_interview(self):
        interview_id = self.interview.id
        self.interview.delete()
        with self.assertRaises(Interview.DoesNotExist):
            Interview.objects.get(id=interview_id)

#Testing Offer Creation.
class OfferModelTests(TestCase):
    def setUp(self):
        self.offer_data = {
            'application_id': 1,
            'salary_offered': 100000,
            'offer_date': '2025-10-01',
            'status': 'Accepted'
        }

    def test_create_offer(self):
        offer = Offer.objects.create(**self.offer_data)
        self.assertEqual(offer.application_id, 1)
        self.assertEqual(offer.salary_offered, 100000)
        self.assertEqual(offer.offer_date, '2025-10-01')
        self.assertEqual(offer.status, 'Accepted')

#Testing Offer update.
class OfferUpdateTests(TestCase):
    def setUp(self):
        self.offer = Offer.objects.create(
            application_id=1,
            salary_offered=100000,
            offer_date='2025-10-01',
            status='Accepted'
        )

    def test_update_offer(self):
        self.offer.status = 'Declined'
        self.offer.save()
        updated_offer = Offer.objects.get(id=self.offer.id)
        self.assertEqual(updated_offer.status, 'Declined')

#Testing Offer Deletion.
class OfferDeleteTests(TestCase):
    def setUp(self):
        self.offer = Offer.objects.create(
            application_id=1,
            salary_offered=100000,
            offer_date='2025-10-01',
            status='Accepted'
        )

    def test_delete_offer(self):
        offer_id = self.offer.id
        self.offer.delete()
        with self.assertRaises(Offer.DoesNotExist):
            Offer.objects.get(id=offer_id)

#Testing Company Creation.
class CompanyModelTests(TestCase):
    def setUp(self):
        self.company_data = {
            'company_name': 'Tech Corp',
            'location': 'San Francisco',
            'industry': 'Technology'
        }

    def test_create_company(self):
        company = Company.objects.create(**self.company_data)
        self.assertEqual(company.company_name, 'Tech Corp')
        self.assertEqual(company.location, 'San Francisco')
        self.assertEqual(company.industry, 'Technology')

#Testing Company update.
class CompanyUpdateTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            company_name='Tech Corp',
            location='San Francisco',
            industry='Technology'
        )

    def test_update_company(self):
        self.company.company_name = 'Tech Innovations'
        self.company.save()
        updated_company = Company.objects.get(id=self.company.id)
        self.assertEqual(updated_company.company_name, 'Tech Innovations')

#Testing Company Deletion.
class CompanyDeleteTests(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            company_name='Tech Corp',
            location='San Francisco',
            industry='Technology'
        )

    def test_delete_company(self):
        company_id = self.company.id
        self.company.delete()
        with self.assertRaises(Company.DoesNotExist):
            Company.objects.get(id=company_id)



