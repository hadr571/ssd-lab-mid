from fastapi import FastAPI, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Base
import app.crud as crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes — Devices
@app.get("/devices/")
def get_devices(db: Session = Depends(get_db)):
    return crud.get_all_devices(db)

@app.post("/devices/")
def create_device(
    name: str = Form(...),
    location: str = Form(...),
    status: bool = Form(...),
    type: str = Form(...),
    db: Session = Depends(get_db)
):
    return crud.add_device(db, name, location, status, type)

@app.put("/devices/{id}")
def update_device(
    id: int,
    name: str = Form(...),
    location: str = Form(...),
    status: bool = Form(...),
    type: str = Form(...),
    db: Session = Depends(get_db)
):
    return crud.update_device(db, id, name, location, status, type)

@app.delete("/devices/{id}")
def delete_device(id: int, db: Session = Depends(get_db)):
    return crud.delete_device(db, id)

# Routes — Users
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db)

@app.post("/users/")
def create_user(
    name: str = Form(...),
    email: str = Form(...),
    role: str = Form(...),
    db: Session = Depends(get_db)
):
    return crud.add_user(db, name, email, role)

@app.put("/users/{id}")
def update_user(
    id: int,
    name: str = Form(...),
    email: str = Form(...),
    role: str = Form(...),
    db: Session = Depends(get_db)
):
    user = crud.update_user(db, id, name, email, role)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User with ID {id} has been deleted"}