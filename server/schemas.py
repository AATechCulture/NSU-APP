from pydantic import BaseModel

# Schema for the passenger class
class PassengerBase(BaseModel):
    seat: str
    drink: str
    wakeup: str

class PassengerCreate(PassengerBase):
    pass

class Passenger(PassengerBase):
    id: int

    class Config:
        orm_mode = True




