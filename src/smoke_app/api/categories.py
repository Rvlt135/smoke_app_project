from typing import List

from fastapi import APIRouter
from .. import tables
from ..database import Session
from ..models.categories import CategoriesModel

router = APIRouter(
    prefix='/categories',
)


@router.get('/', response_model=List[CategoriesModel])
def get_categories_list():
    session = Session()
    categories = (
        session
        .query(tables.CategoriesModel)
        .all
    )
    return categories
