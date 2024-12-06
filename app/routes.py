from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas import JobPostCreate, JobPostResponse
from app.crud import create_job_post, get_job_posts, get_job_post_by_id, delete_job_post

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/jobs", response_model=JobPostResponse)
def create_job(job: JobPostCreate, db: Session = Depends(get_db)):
    return create_job_post(db, job)

@router.get("/jobs", response_model=list[JobPostResponse])
def list_jobs(db: Session = Depends(get_db)):
    return get_job_posts(db)

@router.get("/jobs/{id}", response_model=JobPostResponse)
def read_job(id: int, db: Session = Depends(get_db)):
    job = get_job_post_by_id(db, id)
    if not job:
        raise HTTPException(status_code=404, detail="Job post not found")
    return job

@router.delete("/jobs/{id}")
def delete_job(id: int, db: Session = Depends(get_db)):
    if not delete_job_post(db, id):
        raise HTTPException(status_code=404, detail="Job post not found")
    return {"message": "Job post deleted successfully"}
