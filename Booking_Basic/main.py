from fastapi import FastAPI, HTTPException
from models import Rooms, Update_room

app = FastAPI()

db: list[Rooms] =[
    Rooms(
        id=1,
        user_name="Simbu",
        room_no=101
    ),
    Rooms(
        id=2,
        user_name="John",
        room_no=102
    )
]
@app.get("/")
def root():
    return {"msg": "Welcome to the Hotel Booking API"}

@app.get("/bookings")
def get_all():
    return db

@app.get("/booking/{id}")
def get_detail(id:int):
    for room in db:
        if room.id == id:
            return room
    raise HTTPException(status_code=404, detail=f"Booking id {id} not found")

@app.post("/booking/")
def create_booking(room: Rooms):
    if any(r.room_no == room.room_no for r in db):
        raise HTTPException(status_code=400, detail=f"Room number {room.room_no} already booked")
    if any(r.id == room.id for r in db):
        raise HTTPException(status_code=400, detail=f"Booking id {room.id} already exists")
    db.append(room)
    return room

@app.put("/booking/{id}")
def update_booking(id:int, updated_room: Update_room):
    for room in db:
        if room.id == id:
            if updated_room.user_name is not None:
                room.user_name = updated_room.user_name
            if updated_room.room_no is not None:
                room.room_no = updated_room.room_no
            return {"msg": "Booking updated successfully"}
    raise HTTPException(status_code=404, detail=f"Booking id {id} not found")

@app.delete("/booking/{id}")
def delete_booking(id:int):
    for room in db:
        if room.id == id:
            db.remove(room)
            return {"msg": "Booking deleted successfully"}
    raise HTTPException(status_code=404, detail=f"Booking id {id} not found")