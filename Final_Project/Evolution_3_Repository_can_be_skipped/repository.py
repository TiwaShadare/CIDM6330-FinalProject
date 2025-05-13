from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session, Field, select
import pandas as pd


#SQL Model
class Applicant(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    phone: str
    email: str
    date_applied: str
    experience: str
    status: str
    
class Job(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    location: str
    department: str
    salary: str
    status: str
    posting_date: str
    closing_date: str

class Application(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    job_id: int
    application_date: str
    status: str

class Recruiter(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str
    phone: str
    department: str

class Interview(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    applicant_id: int
    recruiter_id: int
    interview_date: str
    interview_time: str
    interview_status: str

class Offer(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    applicant_id: int
    salary_offered: int
    offer_date: str
    status: str

class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    company_name: str
    location: str
    industry: str


sqlite_file_name = "hrms.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():  
    SQLModel.metadata.create_all(engine)


def create_applicant():
    applicant_1 = Applicant(first_name= "Walter", last_name="White", phone="310-555-5555", email="walterw@yahoo.com", date_applied="01-01-2025", experience="3 Years", status="applied")
    applicant_2 = Applicant(first_name= "Bob", last_name="Dylan", phone="469-595-5656", email="Bobd@gmail.com", date_applied="11-20-2024", experience="5 Years", status="interviewed")
    applicant_3 = Applicant(first_name= "Skylar", last_name="Jenkins", phone="832-111-3333", email="sjenkins@yahoo.com", date_applied="02-02-2025", experience="2 Years", status="applied")
    applicant_4 = Applicant(first_name= "Rita", last_name="Wilson", phone="828-999-4545", email="ritawilson@gmail.com", date_applied="12-01-2024", experience="1 Years", status="interviewed")
    applicant_5 = Applicant(first_name= "Amy", last_name="Powell", phone="212-598-5987", email="amyp123@yahoo.com", date_applied="11-15-2024", experience="6 Years", status="applied")

    session = Session(engine)


    session.add(applicant_1)
    session.add(applicant_2)
    session.add(applicant_3)
    session.add(applicant_4)
    session.add(applicant_5)
    session.commit()

#Read
def select_applicant():
    with Session(engine) as session:
        heroes = session.exec(select(Applicant)).all()
        print(Applicant)

#Update
def update_applicant():
    with Session(engine) as session:
        statement = select(Applicant).where(Applicant.first_name == "Walter")
        results = session.exec(statement)
        hero = results.one()
        print("Applicant:", hero)

        session.add(Applicant)
        session.commit()

def delete_applicant():
    with Session(engine) as session:
        statement = select(Applicant).where(Applicant.first_name == "Amy")
        results = session.exec(statement)
        hero = results.one()
        print("Applicant:", Applicant)

def main():
    create_db_and_tables()


if __name__ == "__main__":
    create_db_and_tables()
    create_applicant()

if __name__ == "__main__":
    main()






#CSV Repo
class CSVRepository:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_data(self):
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            return pd.DataFrame()

    def write_data(self, data: pd.DataFrame):
        data.to_csv(self.file_path, index=False)

    def add_applicant(self, applicant: dict):
        data = self.read_data()
        data = data.append(applicant, ignore_index=True)
        self.write_data(data)

    def get_all_applicants(self):
        return self.read_data().to_dict(orient='Applicants')
    


app = FastAPI()
csv_repo = CSVRepository('data.csv')

class Applicant(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    date_applied: str
    experience: str
    status: str

@app.get("/applicants")
def get_applicants():
    applicants = csv_repo.get_all_applicants()
    return {"applicants": applicants}

@app.post("/applicants")
def add_applicant(applicant: Applicant):
    csv_repo.add_applicant(applicant.dict())
    return {"message": "Applicant added successfully"}


#In Memory Repo
class InMemoryRepository:
    def __init__(self):
        self.applicants = {}
        self.counter = 0

    def add_applicant(self, applicant: Applicant) -> Applicant:
        self.counter += 1
        applicant.id = self.counter
        self.applicants[self.counter] = applicant
        return applicant

    def get_applicant(self, applicant_id: int) -> Applicant:
        return self.applicants.get(applicant_id)

    def update_applicant(self, applicant_id: int, applicant: Applicant) -> Applicant:
        if applicant_id in self.applicants:
            self.applicants[applicant_id] = applicant
            return applicant
        return None

    def delete_applicant(self, applicant_id: int) -> bool:
        if applicant_id in self.applicants:
            del self.applicants[applicant_id]
            return True
        return False

    def list_applicants(self) -> list:
        return list(self.applicants.values())
    

app = FastAPI()
repo = InMemoryRepository()

@app.post("/applicants/", response_model=Applicant)
def create_applicant(applicant: Applicant):
    return repo.add_applicant(applicant)

@app.get("/applicants/{applicant_id}", response_model=Applicant)
def read_applicant(applicant_id: int):
    applicant = repo.get_applicant(applicant_id)
    if applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return applicant

@app.put("/applicants/{applicant_id}", response_model=Applicant)
def update_applicant(applicant_id: int, applicant: Applicant):
    updated_applicant = repo.update_applicant(applicant_id, applicant)
    if updated_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return updated_applicant

@app.delete("/applicants/{applicant_id}", response_model=bool)
def delete_applicant(applicant_id: int):
    success = repo.delete_applicant(applicant_id)
    if not success:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return success

#To run: $uvicorn repository:app --reload