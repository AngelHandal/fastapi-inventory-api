# models.py
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(1000))
    description = Column(String(1000))
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)