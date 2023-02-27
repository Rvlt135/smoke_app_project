from pydantic import BaseModel
from enum import Enum


class CategoriesKind(str, Enum):
    CATEGORY_INDICA = "Indica"
    CATEGORY_SATIVA = "Sativa"
    CATEGORY_HYBRID = "Hybrid"


class CategoriesModel(BaseModel):
    id: int
    name: CategoriesKind
    description: str
