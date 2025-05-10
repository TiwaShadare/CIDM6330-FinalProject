from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Applicant(Base):
    __tablename__ = "Applicants"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    phone = Column(String, index=True)
    email = Column(String, index=True)
    date_applied = Column(String, index=True)
    experience = Column(Integer, index=True)
    status = Column(String, index=True)
    
class Job(Base):
    __tablename__ = "Jobs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    location = Column(String, index=True)
    department = Column(String, index=True)
    salary = Column(String, index=True)
    status = Column(String, index=True)
    posting_date = Column(String, index=True)
    closing_date = Column(String, index=True)

class Application(Base):
    __tablename__ = "Applications"
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, index=True)
    application_date = Column(String, index=True)
    status = Column(String, index=True)

class Recruiter(Base):
    __tablename__ = "Recruiters"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    department = Column(String, index=True)
 
class Interview(Base):
    __tablename__ = "Interviews"
    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, index=True)
    recruiter_id = Column(Integer, index=True)
    interview_date = Column(String, index=True)
    interview_time = Column(String, index=True)
    interview_status = Column(String, index=True)

class Offer(Base):
    __tablename__ = "Offers"
    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, index=True)
    salary_offered = Column(Integer, index=True)
    offer_date = Column(String, index=True)
    status = Column(String, index=True)

class Company(Base):
    __tablename__ = "Company"
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    location = Column(String, index=True)
    industry = Column(String, index=True)