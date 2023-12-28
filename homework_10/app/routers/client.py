from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import database
from models import database as mdb, controller as mct

router = APIRouter(
    prefix="/clients",
    tags=['clients']
)


@router.get('/', response_model=list[mct.Client])
async def get_clients(limit: int = 5, offset: int = 0, db: Session = Depends(database.get_db)):
    return db.query(mdb.Client).all()[offset:offset+limit]


@router.post('/')
async def post_clients():
    return {"message": "post clients"}


@router.put('/')
async def put_clients():
    return {"message": "put clients"}


@router.delete('/')
async def delete_clients():
    return {"message": "delete clients"}


@router.get('/{client_id}')
async def get_client(client_id: int):
    return {"message": f"client {client_id}"}
