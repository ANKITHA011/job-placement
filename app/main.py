from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Posting Microservice")

# Register API routes
app.include_router(router)
