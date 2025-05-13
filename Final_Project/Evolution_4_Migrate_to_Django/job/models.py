from django.db import models

# Create your models here

class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    date_applied = models.DateField(null=True, blank=True)
    experience = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
class Job(models.Model):
    title = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    salary = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100)
    posting_date = models.DateField(null=True, blank=True)
    closing_date = models.DateField(null=True, blank=True)

class Application(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    application_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length = 100)

class Recruiter(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
 
class Interview(models.Model):
    applicant_id = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    recruiter_id = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    interview_date = models.DateField(null=True, blank=True)
    interview_time = models.TimeField(null=True, blank=True)
    interview_status = models.CharField(max_length = 100)

class Offer(models.Model):
    application_id = models.ForeignKey(Application, on_delete=models.CASCADE)
    salary_offered = models.CharField(max_length = 100)
    offer_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length = 100)

class Company(models.Model):
    company_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    industry = models.CharField(max_length = 100)
