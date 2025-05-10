from django.contrib import admin
from .models import Applicant, Job, Application, Recruiter, Interview, Offer, Company


# Register your models here

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "email", "date_applied", "experience", "status")
    list_filter = ("status",)
    search_fields = ("first_name", "last_name", "email")
    ordering = ("last_name",)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "location", "department", "salary", "status", "posting_date", "closing_date")
    list_filter = ("department", "status")
    search_fields = ("title", "location")
    ordering = ("posting_date",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job_id", "application_date", "status")
    list_filter = ("status",)
    search_fields = ("job_id__title",)
    ordering = ("application_date",)

@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "department")
    list_filter = ("department",)
    search_fields = ("first_name", "last_name", "email")
    ordering = ("last_name",)

@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("applicant_id", "recruiter_id", "interview_date", "interview_time", "interview_status")
    list_filter = ("interview_status",)
    search_fields = ("applicant_id__first_name", "recruiter_id__first_name")
    ordering = ("interview_date",)

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("application_id", "salary_offered", "offer_date", "status")
    list_filter = ("status",)
    search_fields = ("application_id__job_id__title",)
    ordering = ("offer_date",)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_name", "location", "industry")
    list_filter = ("industry",)
    search_fields = ("company_name", "location")
    ordering = ("company_name",)