from .models import Device, User
from sqlalchemy.orm import Session

# -----------------------
# Device CRUD
# -----------------------

def get_all_devices(db: Session):
    return db.query(Device).all()

def get_device(db: Session, id: int):
    return db.query(Device).filter(Device.id == id).first()

def add_device(db: Session, name: str, location: str, status: bool, type: str):
    device = Device(name=name, location=location, status=status, type=type)
    db.add(device)
    db.commit()
    db.refresh(device)
    return device

def update_device(db: Session, id: int, name: str, location: str, status: bool, type: str):
    device = get_device(db, id)
    if device:
        device.name = name
        device.location = location
        device.status = status
        device.type = type
        db.commit()
    return device

def delete_device(db: Session, id: int):
    device = get_device(db, id)
    if device:
        db.delete(device)
        db.commit()
    return device

# -----------------------
# User CRUD
# -----------------------

def get_all_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def add_user(db: Session, name: str, email: str, role: str):
    user = User(name=name, email=email, role=role)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, id: int, name: str, email: str, role: str):
    user = get_user(db, id)
    if user:
        user.name = name
        user.email = email
        user.role = role
        db.commit()
    return user

def delete_user(db: Session, id: int):
    user = get_user(db, id)
    if user:
        db.delete(user)
        db.commit()
    return user
