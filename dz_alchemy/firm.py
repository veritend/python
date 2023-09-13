from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from dz_alchemy.database import Base


class Firm(Base):
    __tablename__ = 'firms'

    id = Column(Integer, primary_key=True)
    id_price = Column(Integer, nullable=False)
    clients = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False)
    client = relationship('Client')

    def __init__(self, id_price, count, clients):
        self.id_price = id_price
        self.count = count
        self.clients = clients

    def __repr__(self):
        return f"{self.id},{self.id_price}"f"количество товара: {self.count},"f"покупатель" \
               f" {self.client}, идентификационный номер: "

