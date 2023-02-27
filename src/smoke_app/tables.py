import sqlalchemy as sa
from .database import Base


class Operation(Base):
    __tablename__ = 'category'

    id = sa.Column(sa.Integer, primary_key=True)
    category_name = sa.Column(sa.String)
    slug_categoty_name = sa.Column(sa.String)
