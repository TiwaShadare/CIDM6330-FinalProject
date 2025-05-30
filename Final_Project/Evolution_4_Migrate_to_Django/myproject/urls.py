"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .api import api
from job.views import (
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

app_name = "job"
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/applicants/", ApplicantViewSet.as_view({"get": "list"}), name="applicant-list"),
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]



