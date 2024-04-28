from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status
from uuid import UUID

from api_models import Person
from crud import PersonCRUD
from db import get_db

persons = APIRouter()


@persons.get("/", response_model=list[Person])
def get_persons(db: Session = Depends(get_db)):
    """
    Get all persons
    """
    return PersonCRUD.get_all_persons(db)


@persons.post("/", status_code=status.HTTP_201_CREATED, response_model=Person)
def create_person(person_name: str, db: Session = Depends(get_db)):
    """
    Create a new person
    """
    return PersonCRUD.create(db, person_name)


@persons.get("/{person_id}")
def get_person(person_id: UUID, db: Session = Depends(get_db)):
    """
    Get a person
    """
    test = PersonCRUD.read_by_id(db, person_id)
    return PersonCRUD.read_by_id(db, person_id)
