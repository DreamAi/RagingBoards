from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    image = Column(String)

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String)
    price = Column(Float)
