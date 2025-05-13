from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()



@app.get("/api/greet")
def greet():
    return {"message": "Hello from FastAPI"}

#Applicant Model
class Applicant(BaseModel):
    applicant_id: int
    first_name: str
    last_name: str
    phone: str
    email: str
    date_applied: str
    experience: int 
    status: str

applicants = [
    Applicant(
        applicant_id=1,
        first_name="Walter",
        last_name="White",
        phone="123-456-7890",
        email="walterwhite@yahoo.com",
        date_applied="2025-01-01",
        experience=5,
        status="interviewed",
    ),
    Applicant(
        applicant_id=2,
        first_name="Pamela",
        last_name="White",
        phone="987-654-3210",
        email="pamelawhite@yahoo.com",
        date_applied="2025-01-02",
        experience=3,
        status="offered",
    ),
]

# GET Retrieve all applicants
@app.get("/applicants")
async def get_all_applicants():
    return applicants


# GET Retrieve a applicant by ID
@app.get("/applicants/{applicant_id}")
async def get_applicant_by_id(applicant_id: int):
    applicant = [applicant for applicant in applicants if applicant.applicant_id == applicant_id]
    if applicant:
        return applicant[0]
    else:
        return {"message": f"Applicant with ID {applicant_id} not found"}


# POST Create a new applicant
@app.post("/applicants")
async def create_applicant(applicant: Applicant):
    # Check if applicant ID already exists
    for existing_applicant in applicants:
        if existing_applicant.applicant_id == applicant.applicant_id:
            raise HTTPException(status_code=409, detail= f"Applicant with ID {applicant.applicant_id} already exists. Consider updating.")

    applicants.append(applicant)
    return {"message": "Applicant created successfully", "applicant": applicant}


# PUT Update an existing applicant
@app.put("/applicants/{applicant_id}")
async def update_applicant(applicant_id: int, updated_applicant: Applicant):
    for index, applicant in enumerate(applicants):
        if applicant.applicant_id == applicant_id:
            applicants[index] = updated_applicant
            return {"message": "Applicant updated successfully", "applicant": updated_applicant}
    return {"message": f"Applicant with ID {applicant_id} not found"}

# DELETE Delete an applicant
@app.delete("/applicants/{applicant_id}")
async def delete_applicant(applicant_id: int):
    for index, applicant in enumerate(applicants):
        if applicant.applicant_id == applicant_id:
            deleted_applicant = applicants.pop(index)
            return {"message": "Applicant deleted successfully", "applicant": deleted_applicant}
    return {"message": f"Applicant with ID {applicant_id} not found"}

#Job Model
class Job(BaseModel):
    job_id: int
    title: str
    location: str
    department: str
    salary: str
    status: str
    posting_date: str
    closing_date: str

jobs = [
    Job(
        job_id=1,
        title="Software Engineer",
        location="New York",
        department="Engineering",
        salary="$120,000",
        status="open",
        posting_date="2024-12-01",
        closing_date="2025-01-31",
    ),
    Job(
        job_id=2,
        title="Data Scientist",
        location="San Francisco",
        department="Data Science",
        salary="$130,000",
        status="closed",
        posting_date="2024-12-15",
        closing_date="2025-02-15",
    ),
]

# GET Retrieve all jobs
@app.get("/jobs")
async def get_all_jobs():
    return jobs

# GET Retrieve a job by ID
@app.get("/jobs/{job_id}")
async def get_job_by_id(job_id: int):
    job = [job for job in jobs if job.job_id == job_id]
    if job:
        return job[0]
    else:
        return {"message": f"Job with ID {job_id} not found"}

# POST Create a new job
@app.post("/jobs")
async def create_job(job: Job):
    # Check if job ID already exists
    for existing_job in jobs:
        if existing_job.job_id == job.job_id:
            raise HTTPException(status_code=409, detail= f"Job with ID {job.job_id} already exists. Consider updating.")

    jobs.append(job)
    return {"message": "Job created successfully", "job": job}

# PUT Update an existing job
@app.put("/jobs/{job_id}")
async def update_job(job_id: int, updated_job: Job):
    for index, job in enumerate(jobs):
        if job.job_id == job_id:
            jobs[index] = updated_job
            return {"message": "Job updated successfully", "job": updated_job}
    return {"message": f"Job with ID {job_id} not found"}

# DELETE Delete a job
@app.delete("/jobs/{job_id}")
async def delete_job(job_id: int):
    for index, job in enumerate(jobs):
        if job.job_id == job_id:
            deleted_job = jobs.pop(index)
            return {"message": "Job deleted successfully", "job": deleted_job}
    return {"message": f"Job with ID {job_id} not found"}


#Application Model
class Application(BaseModel):
    application_id: int
    job_id: int
    application_date: str
    status: str 

applications = [
    Application(
        application_id=1,
        job_id=1,
        application_date="2024-12-05",
        status="submitted",
    ),
    Application(
        application_id=2,
        job_id=2,
        application_date="2025-01-10",
        status="interviewed",
    ),
]

# GET Retrieve all applications
@app.get("/applications")
async def get_all_applications():
    return applications

# GET Retrieve an application by ID
@app.get("/applications/{application_id}")
async def get_application_by_id(application_id: int):
    application = [application for application in applications if application.application_id == application_id]
    if application:
        return application[0]
    else:
        return {"message": f"Application with ID {application_id} not found"}

# POST Create a new application
@app.post("/applications")
async def create_application(application: Application):
    # Check if application ID already exists
    for existing_application in applications:
        if existing_application.application_id == application.application_id:
            raise HTTPException(status_code=409, detail= f"Application with ID {application.application_id} already exists. Consider updating.")

    applications.append(application)
    return {"message": "Application created successfully", "application": application}

# PUT Update an existing application
@app.put("/applications/{application_id}")
async def update_application(application_id: int, updated_application: Application):
    for index, application in enumerate(applications):
        if application.application_id == application_id:
            applications[index] = updated_application
            return {"message": "Application updated successfully", "application": updated_application}
    return {"message": f"Application with ID {application_id} not found"}

# DELETE Delete an application
@app.delete("/applications/{application_id}")
async def delete_application(application_id: int):
    for index, application in enumerate(applications):
        if application.application_id == application_id:
            deleted_application = applications.pop(index)
            return {"message": "Application deleted successfully", "application": deleted_application}
    return {"message": f"Application with ID {application_id} not found"}

#Interview Model
class Interview(BaseModel):
    interview_id: int
    applicant_id: int
    recruiter_id: int
    interview_date: str
    interview_time: str
    interview_status: str

interviews = [
    Interview(
        interview_id=1,
        applicant_id=1,
        recruiter_id=1,
        interview_date="2025-03-20",
        interview_time="10:00 AM",
        interview_status="scheduled",
    ),
    Interview(
        interview_id=2,
        applicant_id=2,
        recruiter_id=2,
        interview_date="2025-02-25",
        interview_time="02:00 PM",
        interview_status="completed",
    ),
]

# GET Retrieve all interviews
@app.get("/interviews")
async def get_all_interviews():
    return interviews

# GET Retrieve an interview by ID
@app.get("/interviews/{interview_id}")
async def get_interview_by_id(interview_id: int):
    interview = [interview for interview in interviews if interview.interview_id == interview_id]
    if interview:
        return interview[0]
    else:
        return {"message": f"Interview with ID {interview_id} not found"}
    
# POST Create a new interview
@app.post("/interviews")
async def create_interview(interview: Interview):
    # Check if interview ID already exists
    for existing_interview in interviews:
        if existing_interview.interview_id == interview.interview_id:
            raise HTTPException(status_code=409, detail= f"Interview with ID {interview.interview_id} already exists. Consider updating.")

    interviews.append(interview)
    return {"message": "Interview created successfully", "interview": interview}

# PUT Update an existing interview
@app.put("/interviews/{interview_id}")
async def update_interview(interview_id: int, updated_interview: Interview):
    for index, interview in enumerate(interviews):
        if interview.interview_id == interview_id:
            interviews[index] = updated_interview
            return {"message": "Interview updated successfully", "interview": updated_interview}
    return {"message": f"Interview with ID {interview_id} not found"}

# DELETE Delete an interview
@app.delete("/interviews/{interview_id}")
async def delete_interview(interview_id: int):
    for index, interview in enumerate(interviews):
        if interview.interview_id == interview_id:
            deleted_interview = interviews.pop(index)
            return {"message": "Interview deleted successfully", "interview": deleted_interview}
    return {"message": f"Interview with ID {interview_id} not found"}

#Offer Model
class Offer(BaseModel):
    offer_id: int
    application_id: int
    salary_offered: int
    offer_date: str
    status: str

offers = [
    Offer(
        offer_id=1,
        application_id=1,
        salary_offered=120000,
        offer_date="2024-10-15",
        status="accepted",
    ),
    Offer(
        offer_id=2,
        application_id=2,
        salary_offered=130000,
        offer_date="2024-09-20",
        status="declined",
    ),
]

# GET Retrieve all offers
@app.get("/offers")
async def get_all_offers():
    return offers

# GET Retrieve an offer by ID
@app.get("/offers/{offer_id}")
async def get_offer_by_id(offer_id: int):
    offer = [offer for offer in offers if offer.offer_id == offer_id]
    if offer:
        return offer[0]
    else:
        return {"message": f"Offer with ID {offer_id} not found"}
    
# POST Create a new offer
@app.post("/offers")
async def create_offer(offer: Offer):
    # Check if offer ID already exists
    for existing_offer in offers:
        if existing_offer.offer_id == offer.offer_id:
            raise HTTPException(status_code=409, detail= f"Offer with ID {offer.offer_id} already exists. Consider updating.")

    offers.append(offer)
    return {"message": "Offer created successfully", "offer": offer}

# PUT Update an existing offer
@app.put("/offers/{offer_id}")
async def update_offer(offer_id: int, updated_offer: Offer):
    for index, offer in enumerate(offers):
        if offer.offer_id == offer_id:
            offers[index] = updated_offer
            return {"message": "Offer updated successfully", "offer": updated_offer}
    return {"message": f"Offer with ID {offer_id} not found"}

# DELETE Delete an offer
@app.delete("/offers/{offer_id}")
async def delete_offer(offer_id: int):
    for index, offer in enumerate(offers):
        if offer.offer_id == offer_id:
            deleted_offer = offers.pop(index)
            return {"message": "Offer deleted successfully", "offer": deleted_offer}
    return {"message": f"Offer with ID {offer_id} not found"}



#Recruiter Model
class Recruiter(BaseModel):
    recruiter_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    department: str

recruiters = [
    Recruiter(
        recruiter_id=1,
        first_name="Tiwa",
        last_name="Shadare",
        email="Tiwa.shadare@example.com",
        phone="123-456-7890",
        department="Engineering",
    ),
    Recruiter(
        recruiter_id=2,
        first_name="Skylar",
        last_name="Taylor",
        email="skylartaylor@gmail.com",
        phone="987-654-3210",
        department="Data Science",
    ),  

]

# GET Retrieve all recruiters
@app.get("/recruiters") 
async def get_all_recruiters():
    return recruiters

# GET Retrieve a recruiter by ID
@app.get("/recruiters/{recruiter_id}")
async def get_recruiter_by_id(recruiter_id: int):
    recruiter = [recruiter for recruiter in recruiters if recruiter.recruiter_id == recruiter_id]
    if recruiter:
        return recruiter[0]
    else:
        return {"message": f"Recruiter with ID {recruiter_id} not found"}
    
# POST Create a new recruiter
@app.post("/recruiters")
async def create_recruiter(recruiter: Recruiter):
    # Check if recruiter ID already exists
    for existing_recruiter in recruiters:
        if existing_recruiter.recruiter_id == recruiter.recruiter_id:
            raise HTTPException(status_code=409, detail= f"Recruiter with ID {recruiter.recruiter_id} already exists. Consider updating.")

    recruiters.append(recruiter)
    return {"message": "Recruiter created successfully", "recruiter": recruiter}

# PUT Update an existing recruiter
@app.put("/recruiters/{recruiter_id}")
async def update_recruiter(recruiter_id: int, updated_recruiter: Recruiter):
    for index, recruiter in enumerate(recruiters):
        if recruiter.recruiter_id == recruiter_id:
            recruiters[index] = updated_recruiter
            return {"message": "Recruiter updated successfully", "recruiter": updated_recruiter}
    return {"message": f"Recruiter with ID {recruiter_id} not found"}

# DELETE Delete a recruiter
@app.delete("/recruiters/{recruiter_id}")
async def delete_recruiter(recruiter_id: int):
    for index, recruiter in enumerate(recruiters):
        if recruiter.recruiter_id == recruiter_id:
            deleted_recruiter = recruiters.pop(index)
            return {"message": "Recruiter deleted successfully", "recruiter": deleted_recruiter}
    return {"message": f"Recruiter with ID {recruiter_id} not found"}

#Company Model
class Company(BaseModel):
    company_id: int
    company_name: str
    location: str
    industry: str

companys = [
    Company(
        company_id=1,
        company_name="TechCorp",
        location="San Francisco",
        industry="Technology",
    ),
    Company(
        company_id=2,
        company_name="DataSolutions",
        location="New York",
        industry="Data Analytics",
    ),
]

# GET Retrieve all companies
@app.get("/companys")
async def get_all_companys():
    return companys

# GET Retrieve a company by ID
@app.get("/companys/{company_id}")
async def get_company_by_id(company_id: int):
    company = [company for company in companys if company.company_id == company_id]
    if company:
        return company[0]
    else:
        return {"message": f"Company with ID {company_id} not found"}
    

# POST Create a new company
@app.post("/companys")
async def create_company(company: Company):
    # Check if company ID already exists
    for existing_company in companys:
        if existing_company.company_id == company.company_id:
            raise HTTPException(status_code=409, detail= f"Company with ID {company.company_id} already exists. Consider updating.")
    
    companys.append(company)
    return {"message": "Company created successfully", "company": company}

# PUT Update an existing company
@app.put("/companys/{company_id}")
async def update_company(company_id: int, updated_company: Company):
    for index, company in enumerate(companys):
        if company.company_id == company_id:
            companys[index] = updated_company
            return {"message": "Company updated successfully", "company": updated_company}
    return {"message": f"Company with ID {company_id} not found"}

#DELETE Delete a company
@app.delete("/companys/{company_id}")
async def delete_company(company_id: int):
    for index, company in enumerate(companys):
        if company.company_id == company_id:
            deleted_company = companys.pop(index)
            return {"message": "Company deleted successfully", "company": deleted_company}
    return {"message": f"Company with ID {company_id} not found"}



# To run the application, use the command: uvicorn main:app --reload

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)





