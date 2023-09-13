from sqlalchemy import Column, ForeignKey, Integer, String

from dz_alchemy.database import Base


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    model = Column(String(100), nullable=False)
    goods = Column(String(100), nullable=False)
    count = Column(Integer, nullable=False)
    price_count = Column(Integer, nullable=False)
    # id_price = Column(Integer)
    id_price = Column(Integer, ForeignKey('firms.id'))

    def __init__(self, model, goods, count, price_count, id_price):
        self.model = model
        self.goods = goods
        self.count = count
        self.price_count = price_count
        self.id_price = id_price

    def __repr__(self):
        return f"Модель: {self.model}, товар: {self.goods}, количество: {self.count}, цена: {self.price_count}," \
               f"идентификационный номер товара: {self.id_price}"
