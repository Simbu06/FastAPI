from fastapi import FastAPI, HTTPException
from models import User, UpdateUser, Gender


app = FastAPI()

db: list[User] = [
    User(
        id= 1,
        name= 'Simbu',
        email= 'silambu@gmail.com',
        gender= Gender.Male,
        mobile_no= 9345044366
    )
]

@app.get('/users')
def get_users():
    return db

@app.get('/user/{id}')
def user(id:int):
    for user in db:
        if user.id == id:
            return user
    raise HTTPException(status_code=400, detail="User with id not found")

@app.post('/user')
def create_user(user:User):
    if any(user.id == u.id for u in db):
        raise HTTPException(status_code=400, detail="User with given ID already exists")
    db.append(user)
    return db

@app.put('/user/{id}')
def update_user(id:int, user:UpdateUser):
    for r in db:
        if r.id == id:
            if user.name is not None:
                r.name = user.name
            if user.email is not None:
                r.email = user.email
            if user.gender is not None:
                r.gender = user.gender
            if user.mobile_no is not None:
                r.mobile_no = user.mobile_no
            return r
    else:
        raise HTTPException(status_code=400, detail="User with id not found")
    
@app.delete('/user/{id}')
def delete_user(id:int):
    for user in db:
        if id == user.id:
            db.remove(user)
            return('User has been deleted')
    raise HTTPException(status_code=400, detail="User with id not found")
            