from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
import schemas
import database


app = FastAPI()


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Applicant Routes
#Create (Post) Applicant
@app.post("/applicants/", response_model=schemas.Applicant)
def create_applicant(applicant: schemas.ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = models.Applicant(name=applicant.name, description=applicant.description)
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

#Read (Get) Applicant
@app.get("/applicants/{applicant_id}", response_model=schemas.Applicant)
def read_applicant(applicant_id: int, db: Session = Depends(get_db)):
    db_applicant = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return db_applicant

#Update (Put) Applicant
@app.put("/applicants/{applicant_id}", response_model=schemas.Applicant)
def update_applicant(applicant_id: int, applicant: schemas.ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    db_applicant.name = applicant.name
    db_applicant.description = applicant.description
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

#Delete Applicant
@app.delete("/applicants/{applicant_id}", response_model=schemas.Applicant)
def delete_applicant(applicant_id: int, db: Session = Depends(get_db)):
    db_applicant = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    db.delete(db_applicant)
    db.commit()
    return db_applicant

#Job Routes
#Create (Post) Job
@app.post("/jobs/", response_model=schemas.Job)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = models.Job(name=job.name, description=job.description)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

#Read (Get) Job
@app.get("/jobs/{job_id}", response_model=schemas.Job)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

#Update (put) Job
@app.put("/jobs/{job_id}", response_model=schemas.Job)
def update_job(job_id: int, job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    db_job.name = job.name
    db_job.description = job.description
    db.commit()
    db.refresh(db_job)
    return db_job

#Delete Job
@app.delete("/jobs/{job_id}", response_model=schemas.Job)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return db_job


#Application Routes
#Create (Post) Application
@app.post("/applications/", response_model=schemas.Application)
def create_application(application: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    db_application = models.Application(name=application.name, description=application.description)
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

#Read (Get) Application
@app.get("/applications/{application_id}", response_model=schemas.Application)
def read_application(application_id: int, db: Session = Depends(get_db)):
    db_application = db.query(models.Application).filter(models.Application.id == application_id).first()
    if db_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    return db_application

#Update (put) Application
@app.put("/applications/{application_id}", response_model=schemas.Application)
def update_application(application_id: int, application: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    db_application = db.query(models.Application).filter(models.Application.id == application_id).first()
    if db_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db_application.name = application.name
    db_application.description = application.description
    db.commit()
    db.refresh(db_application)
    return db_application

#Delete Application
@app.delete("/applications/{application_id}", response_model=schemas.Application)
def delete_application(application_id: int, db: Session = Depends(get_db)):
    db_application = db.query(models.Application).filter(models.Application.id == application_id).first()
    if db_application is None:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(db_application)
    db.commit()
    return db_application

#offer Routes
#Create (Post) offer
@app.post("/offers/", response_model=schemas.Offer)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    db_offer = models.Offer(name=offer.name, description=offer.description)
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

#Read (Get) offer
@app.get("/offers/{offer_id}", response_model=schemas.Offer)
def read_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    return db_offer

#Update (put) offer
@app.put("/offers/{offer_id}", response_model=schemas.Offer)
def update_offer(offer_id: int, offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    db_offer.name = offer.name
    db_offer.description = offer.description
    db.commit()
    db.refresh(db_offer)
    return db_offer

#Delete offer
@app.delete("/offers/{offer_id}", response_model=schemas.Offer)
def delete_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = db.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    db.delete(db_offer)
    db.commit()
    return db_offer


#Interview Routes
#Create (Post) Interview
@app.post("/interviews/", response_model=schemas.Interview)
def create_interview(interview: schemas.InterviewCreate, db: Session = Depends(get_db)):
    db_interview = models.Interview(name=interview.name, description=interview.description)
    db.add(db_interview)
    db.commit()
    db.refresh(db_interview)
    return db_interview

#Read (Get) Interview
@app.get("/interviews/{interview_id}", response_model=schemas.Interview)
def read_interview(interview_id: int, db: Session = Depends(get_db)):
    db_interview = db.query(models.Interview).filter(models.Interview.id == interview_id).first()
    if db_interview is None:
        raise HTTPException(status_code=404, detail="Interview not found")
    return db_interview

#Update (put) Interview
@app.put("/interviews/{interview_id}", response_model=schemas.Interview)
def update_interview(interview_id: int, interview: schemas.InterviewCreate, db: Session = Depends(get_db)):
    db_interview = db.query(models.Interview).filter(models.Interview.id == interview_id).first()
    if db_interview is None:
        raise HTTPException(status_code=404, detail="Interview not found")
    db_interview.name = interview.name
    db_interview.description = interview.description
    db.commit()
    db.refresh(db_interview)
    return db_interview

#Delete Interview
@app.delete("/interviews/{interview_id}", response_model=schemas.Interview)
def delete_interview(interview_id: int, db: Session = Depends(get_db)):
    db_interview = db.query(models.Interview).filter(models.Interview.id == interview_id).first()
    if db_interview is None:
        raise HTTPException(status_code=404, detail="Interview not found")
    db.delete(db_interview)
    db.commit()
    return db_interview


#Recruiter Routes
#Create (Post) Recruiter
@app.post("/recruiters/", response_model=schemas.Recruiter)
def create_recruiter(recruiter: schemas.RecruiterCreate, db: Session = Depends(get_db)):
    db_recruiter = models.Recruiter(name=recruiter.name, description=recruiter.description)
    db.add(db_recruiter)
    db.commit()
    db.refresh(db_recruiter)
    return db_recruiter

#Read (Get) Recruiter
@app.get("/recruiters/{recruiter_id}", response_model=schemas.Recruiter)
def read_recruiter(recruiter_id: int, db: Session = Depends(get_db)):
    db_recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == recruiter_id).first()
    if db_recruiter is None:
        raise HTTPException(status_code=404, detail="Recruiter not found")
    return db_recruiter

#Update (put) Recruiter
@app.put("/recruiters/{recruiter_id}", response_model=schemas.Recruiter)
def update_recruiter(recruiter_id: int, recruiter: schemas.RecruiterCreate, db: Session = Depends(get_db)):
    db_recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == recruiter_id).first()
    if db_recruiter is None:
        raise HTTPException(status_code=404, detail="Recruiter not found")
    db_recruiter.name = recruiter.name
    db_recruiter.description = recruiter.description
    db.commit()
    db.refresh(db_recruiter)
    return db_recruiter

#Delete Recruiter
@app.delete("/recruiters/{recruiter_id}", response_model=schemas.Recruiter)
def delete_recruiter(recruiter_id: int, db: Session = Depends(get_db)):
    db_recruiter = db.query(models.Recruiter).filter(models.Recruiter.id == recruiter_id).first()
    if db_recruiter is None:
        raise HTTPException(status_code=404, detail="Recruiter not found")
    db.delete(db_recruiter)
    db.commit()
    return db_recruiter


#Company Routes
#Create (Post) Company
@app.post("/companys/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = models.Company(name=company.name, description=company.description)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

#Read (Get) Company
@app.get("/companys/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

#Update (put) Company
@app.put("/companys/{company_id}", response_model=schemas.Company)
def update_company(company_id: int, company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    db_company.name = company.name
    db_company.description = company.description
    db.commit()
    db.refresh(db_company)
    return db_company

#Delete Company
@app.delete("/companys/{company_id}", response_model=schemas.Company)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if db_company is None:
        raise HTTPException(status_code=404, detail="company not found")
    db.delete(db_company)
    db.commit()
    return db_company

#To run: $uvicorn main:app --reload