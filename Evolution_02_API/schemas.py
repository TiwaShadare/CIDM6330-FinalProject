from pydantic import BaseModel

class ApplicantBase(BaseModel):
    name: str
    description: str

class ApplicantCreate(ApplicantBase):
    pass

class Applicant(ApplicantBase):
    id: int

    class Config:
        orm_mode = True


class JobBase(BaseModel):
    name: str
    description: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True


class ApplicationBase(BaseModel):
    name: str
    description: str

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int

    class Config:
        orm_mode = True        


class RecruiterBase(BaseModel):
    name: str
    description: str

class RecruiterCreate(RecruiterBase):
    pass

class Recruiter(RecruiterBase):
    id: int

    class Config:
        orm_mode = True


class InterviewBase(BaseModel):
    name: str
    description: str

class InterviewCreate(InterviewBase):
    pass

class Interview(InterviewBase):
    id: int

    class Config:
        orm_mode = True


class OfferBase(BaseModel):
    name: str
    description: str

class OfferCreate(OfferBase):
    pass

class Offer(OfferBase):
    id: int

    class Config:
        orm_mode = True


class CompanyBase(BaseModel):
    name: str
    description: str

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int

    class Config:
        orm_mode = True