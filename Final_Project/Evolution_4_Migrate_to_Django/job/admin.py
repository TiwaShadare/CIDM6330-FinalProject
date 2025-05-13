from django.contrib import admin

from .models import Applicant, Job, Application, Recruiter, Interview, Offer, Company


# Register your models here

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "phone",
        "email",
        "date_applied",
        "experience",
        "status",
    ]
def get_applicant_name(self, obj):
        """Returns the full name of the applicant."""
        return f"{obj.first_name} {obj.last_name}"

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "location",
        "department",
        "salary",
        "status",
        "posting_date",
        "closing_date",
    ]
    def get_job_title(self, obj):
        """Returns the title of the job."""
        return obj.title
    
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [
        "job_id",
        "application_date",
        "status",
    ]
    def get_application_date(self, obj):
        """Returns the date of application."""
        return obj.application_date

@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "email",
        "phone",
        "department",
    ]
    def get_recruiter_name(self, obj):
        """Returns the full name of the recruiter."""
        return f"{obj.first_name} {obj.last_name}"

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = [
        "applicant_id",
        "recruiter_id",
        "interview_date",
        "interview_time",
        "interview_status",
    ]
    def get_interview_date(self, obj):
        """Returns the date of the interview."""
        return obj.interview_date
    
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = [
        "application_id",
        "salary_offered",
        "offer_date",
        "status",
    ]
    def get_offer_date(self, obj):
        """Returns the date of the offer."""
        return obj.offer_date
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "company_name",
        "location",
        "industry",
    ]
    def get_company_name(self, obj):
        """Returns the name of the company."""
        return obj.company_name 
