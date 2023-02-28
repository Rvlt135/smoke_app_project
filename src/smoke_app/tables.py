import sqlalchemy as sa
from .database import Base


class CategoriesModel(Base):
    __tablename__ = 'categories'

    id = sa.Column(sa.Integer, primary_key=True)
    category_name = sa.Column(sa.String)
    slug_category_name = sa.Column(sa.String)
    rating = sa.Column(sa.Integer)


"""class CategoriesModel:
    pass"""