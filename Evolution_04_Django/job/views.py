from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Applicant, Job, Application, Recruiter, Interview, Offer, Company
from .tasks import send_welcome_email

# Create your views here.
from .serializers import (
    ApplicantSerializer,
    JobSerializer,
    ApplicationSerializer,
    RecruiterSerializer,
    InterviewSerializer,
    OfferSerializer,
    CompanySerializer,
)


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    @action(detail=True, methods=["post"])
    def send_welcome_email(self, request, pk=None):
        applicant = self.get_object()
        send_welcome_email.delay(applicant.id)
        return Response({"status": "Email sent"}, status=status.HTTP_200_OK)
    
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class RecruiterViewSet(viewsets.ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer    