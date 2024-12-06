from sqlalchemy.orm import Session
from app.models import JobPost
from app.schemas import JobPostCreate

def create_job_post(db: Session, job: JobPostCreate):
    db_job = JobPost(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def get_job_posts(db: Session):
    return db.query(JobPost).all()

def get_job_post_by_id(db: Session, job_id: int):
    return db.query(JobPost).filter(JobPost.id == job_id).first()

def delete_job_post(db: Session, job_id: int):
    db_job = db.query(JobPost).filter(JobPost.id == job_id).first()
    if db_job:
        db.delete(db_job)
        db.commit()
        return True
    return False
