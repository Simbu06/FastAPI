from pydantic import BaseModel
from typing import Optional


class Rooms(BaseModel):
    id:int
    user_name: str
    room_no: int
    
class Update_room(BaseModel):
    user_name: Optional[str] = None
    room_no: Optional[int] = None