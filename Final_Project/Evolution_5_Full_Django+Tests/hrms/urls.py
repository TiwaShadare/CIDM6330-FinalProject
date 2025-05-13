from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .api import api
from . import views
from hrms.views import (
    ApplicantViewSet,
    JobViewSet,
    ApplicationViewSet,
    RecruiterViewSet,
    InterviewViewSet,
    OfferViewSet,
    CompanyViewSet,
)


# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r"applicants", ApplicantViewSet)
router.register(r"jobs", JobViewSet)
router.register(r"applications", ApplicationViewSet)
router.register(r"recruiters", RecruiterViewSet)
router.register(r"interviews", InterviewViewSet)
router.register(r"offers", OfferViewSet)
router.register(r"companies", CompanyViewSet)

app_name = "hrms"
urlpatterns = [
    path('', views.index, name='index'), 
    path("api/v1/", include(router.urls)),
    path("api/v1/applicants/", ApplicantViewSet.as_view({"get": "list"}), name="applicant-list"),
    path('admin/', admin.site.urls),
    path("api/", api.urls),
    path('', include("hrms.urls")),
]



