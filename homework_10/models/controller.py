from pydantic import BaseModel


class Client(BaseModel):
    client_id: int
    document: str
    first_name: str
    last_name: str
    patronymic: str
    birthday: float


class Consultation(BaseModel):
    consultation_id: int
    client_id: int
    pet_id: int
    date: float
    description: str


class Pet(BaseModel):
    pet_id: int
    client_id: int
    name: str
    birthday: float
