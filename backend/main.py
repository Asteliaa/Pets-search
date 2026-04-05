from fastapi import FastAPI
from backend.core.database import engine, Base
from backend.api.routes_report import router as routes_report
from backend.api.routes_users import router as routes_users
from backend.api.routes_photo import router as routes_photo
from backend.models import user, report, photo


app = FastAPI(title="Pets API", version="1.0")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine) #, checkfirst=True
    

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pets API!"}


@app.get("/health")
def health():
    return {"status": "ok"}    



app.include_router(routes_report)
app.include_router(routes_users)
app.include_router(routes_photo)