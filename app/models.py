from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class JobPost(Base):
    __tablename__ = "job_posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)
    company = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
