from typing import List

from fastapi import APIRouter
from ..models.categories import CategoriesModel

router = APIRouter(
    prefix='/categories',
)


@router.get('/', response_model=List[CategoriesModel])
def get_categories_list():
    return []