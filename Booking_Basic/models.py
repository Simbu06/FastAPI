from pydantic import BaseModel


class Rooms(BaseModel):
    id:int
    user_name: str
    room_no: int
    
class Update_room(BaseModel):
    user_name: str| None = None
    room_no: int| None = None