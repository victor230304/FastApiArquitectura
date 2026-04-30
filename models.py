from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Coche(Base):
    __tablename__ = "coches"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, index=True)
    modelo = Column(String, nullable=True)
    año = Column(Integer)
    precio = Column(Float)
    disponible = Column(Boolean, default=True)