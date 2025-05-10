from datetime import date
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from ninja import Schema
from hrms.models import Applicant, Job, Application, Recruiter, Interview, Offer, Company


api=NinjaAPI()

@api.get("/hello")
def hello(request):
    return {"message": "Hello, World!"}

@api.get("/add")
def add(request, a: int, b:int):
    return{"result": a + b}


# This is an input schema for the Applicant model
class ApplicantIn(Schema):
    first_name: str
    last_name: str
    phone: str
    email: str
    date_applied: date
    experience: str
    status: str
   

class ApplicantOut(Schema):
    id: int
    first_name: str
    last_name: str
    phone: str
    email: str
    date_applied: date
    experience: str
    status: str


@api.post("/applicants")
def create_applicant(request, payload: ApplicantIn):
    applicant = Applicant(**payload.dict()) # Create a new Applicant instance.  
    applicant.save()
    return {"success": True, "applicant": applicant}    


@api.get("/applicants/{applicant_id}", response=ApplicantOut)
def get_applicant(request, applicant_id: int):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    return applicant


@api.put("/applicants/{applicant_id}")
def update_applicant(request, applicant_id: int, payload: ApplicantIn):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    for attr, value in payload.dict().items():
        setattr(applicant, attr, value)
    applicant.save()
    return {"success": True, "applicant": applicant}    

@api.delete("/applicants/{applicant_id}")
def delete_applicant(request, applicant_id: int):
    applicant = get_object_or_404(Applicant, id=applicant_id)
    applicant.delete()
    return {"success": True, "applicant": applicant}    


# This is an input schema for the Job model
class JobIn(Schema):    
    title: str
    location: str
    department: str
    salary: str
    status: str
    posting_date: date
    closing_date: date

class JobOut(Schema):
    id: int
    title: str
    location: str
    department: str
    salary: str 
    status: str
    posting_date: date
    closing_date: date

@api.post("/jobs")
def create_job(request, payload: JobIn):
    job = Job(**payload.dict()) # Create a new Job instance   
    job.save()
    return {"success": True, "job": job}

@api.get("/jobs/{job_id}", response=JobOut)
def get_job(request, job_id: int):
    job = get_object_or_404(Job, id=job_id)
    return job

@api.put("/jobs/{job_id}")
def update_job(request, job_id: int, payload: JobIn):
    job = get_object_or_404(Job, id=job_id)
    for attr, value in payload.dict().items():
        setattr(job, attr, value)
    job.save()
    return {"success": True, "job": job}

@api.delete("/jobs/{job_id}")
def delete_job(request, job_id: int):
    job = get_object_or_404(Job, id=job_id)
    job.delete()
    return {"success": True, "job": job}

# This is an input schema for the Application model
class ApplicationIn(Schema):    
    job_id: int
    application_date: date
    status: str 

class ApplicationOut(Schema):
    id: int
    job_id: int
    application_date: date
    status: str

@api.post("/applications")
def create_application(request, payload: ApplicationIn):
    application = Application(**payload.dict()) # Create a new Application instance   
    application.save()
    return {"success": True, "application": application}

@api.get("/applications/{application_id}", response=ApplicationOut)
def get_application(request, application_id: int):
    application = get_object_or_404(Application, id=application_id)
    return application

@api.put("/applications/{application_id}")
def update_application(request, application_id: int, payload: ApplicationIn):
    application = get_object_or_404(Application, id=application_id)
    for attr, value in payload.dict().items():
        setattr(application, attr, value)
    application.save()
    return {"success": True, "application": application}

@api.delete("/applications/{application_id}")
def delete_application(request, application_id: int):
    application = get_object_or_404(Application, id=application_id)
    application.delete()
    return {"success": True, "application": application}


 # This is an input schema for the Recruiter model
class RecruiterIn(Schema):
    first_name: str
    last_name: str
    email: str
    phone: str
    department: str

class RecruiterOut(Schema):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    department: str

@api.post("/recruiters")
def create_recruiter(request, payload: RecruiterIn):
    recruiter = Recruiter(**payload.dict()) # Create a new Recruiter instance   
    recruiter.save()
    return {"success": True, "recruiter": recruiter}

@api.get("/recruiters/{recruiter_id}", response=RecruiterOut)
def get_recruiter(request, recruiter_id: int):
    recruiter = get_object_or_404(Recruiter, id=recruiter_id)
    return recruiter

@api.put("/recruiters/{recruiter_id}")
def update_recruiter(request, recruiter_id: int, payload: RecruiterIn):
    recruiter = get_object_or_404(Recruiter, id=recruiter_id)
    for attr, value in payload.dict().items():
        setattr(recruiter, attr, value)
    recruiter.save()
    return {"success": True, "recruiter": recruiter}

@api.delete("/recruiters/{recruiter_id}")
def delete_recruiter(request, recruiter_id: int):
    recruiter = get_object_or_404(Recruiter, id=recruiter_id)
    recruiter.delete()
    return {"success": True, "recruiter": recruiter}

# This is an input schema for the Interview model
class InterviewIn(Schema):  
    applicant_id: int
    recruiter_id: int
    interview_date: date
    interview_time: str
    interview_status: str

class InterviewOut(Schema):
    id: int
    applicant_id: int
    recruiter_id: int
    interview_date: date    
    interview_time: str
    interview_status: str   

@api.post("/interviews")
def create_interview(request, payload: InterviewIn):
    interview = Interview(**payload.dict()) # Create a new Interview instance   
    interview.save()
    return {"success": True, "interview": interview}

@api.get("/interviews/{interview_id}", response=InterviewOut)
def get_interview(request, interview_id: int):
    interview = get_object_or_404(Interview, id=interview_id)
    return interview

@api.put("/interviews/{interview_id}")
def update_interview(request, interview_id: int, payload: InterviewIn):
    interview = get_object_or_404(Interview, id=interview_id)
    for attr, value in payload.dict().items():
        setattr(interview, attr, value)
    interview.save()
    return {"success": True, "interview": interview}

@api.delete("/interviews/{interview_id}")
def delete_interview(request, interview_id: int):
    interview = get_object_or_404(Interview, id=interview_id)
    interview.delete()
    return {"success": True, "interview": interview}


# This is an input schema for the Offer model
class OfferIn(Schema):
    application_id: int
    salary_offered: str
    offer_date: date
    status: str

class OfferOut(Schema):
    id: int
    application_id: int
    salary_offered: str
    offer_date: date
    status: str

@api.post("/offers")
def create_offer(request, payload: OfferIn):
    offer = Offer(**payload.dict()) # Create a new Offer instance   
    offer.save()
    return {"success": True, "offer": offer}

@api.get("/offers/{offer_id}", response=OfferOut)
def get_offer(request, offer_id: int):
    offer = get_object_or_404(Offer, id=offer_id)
    return offer

@api.put("/offers/{offer_id}")
def update_offer(request, offer_id: int, payload: OfferIn):
    offer = get_object_or_404(Offer, id=offer_id)
    for attr, value in payload.dict().items():
        setattr(offer, attr, value)
    offer.save()
    return {"success": True, "offer": offer}

@api.delete("/offers/{offer_id}")
def delete_offer(request, offer_id: int):
    offer = get_object_or_404(Offer, id=offer_id)
    offer.delete()
    return {"success": True, "offer": offer}

# This is an input schema for the Company model
class CompanyIn(Schema):
    company_name: str
    location: str
    industry: str

class CompanyOut(Schema):
    id: int
    company_name: str
    location: str
    industry: str

@api.post("/companies")
def create_company(request, payload: CompanyIn):
    company = Company(**payload.dict()) # Create a new Company instance   
    company.save()
    return {"success": True, "company": company}

@api.get("/companies/{company_id}", response=CompanyOut)
def get_company(request, company_id: int):
    company = get_object_or_404(Company, id=company_id)
    return company

@api.put("/companies/{company_id}")
def update_company(request, company_id: int, payload: CompanyIn):
    company = get_object_or_404(Company, id=company_id)
    for attr, value in payload.dict().items():
        setattr(company, attr, value)
    company.save()
    return {"success": True, "company": company}

@api.delete("/companies/{company_id}")
def delete_company(request, company_id: int):
    company = get_object_or_404(Company, id=company_id)
    company.delete()
    return {"success": True, "company": company}








