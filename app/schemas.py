from pydantic import BaseModel

class JobPostCreate(BaseModel):
    title: str
    description: str
    location: str
    company: str
    salary: float

class JobPostResponse(JobPostCreate):
    id: int

    class Config:
        orm_mode = True
