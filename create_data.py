from faker import Faker

from dz_alchemy.database import create_db, Session
from dz_alchemy.client import Client
from dz_alchemy.firm import Firm


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    models_list = [
        'TWS Sennheiser CX Plus True Wireless',
        'Fifine K658',
        'Canon EOS M200 Kit 15-45mm IS STM',
        'GameLab Monolith GL-900',
        'ASUS TUF Gaming F15 FX506HC-HN004',
    ]
    goods_list = ['наушники', 'микрофон', 'беззеркальная камера', 'стол', 'ноутбук']
    prices_list = [13799, 7499, 70999, 12499, 79999]
    id_prices = [501, 486, 918, 738, 624]
    client_list = [
        'Цветков Илья Максимович',
        'Захаров Платон Миронович',
        'Селиванова София Кирилловна',
        'Родионова Александра Александровна',
        'Кузнецов Максим Александрович',
    ]

    faker = Faker("ru_RU")
    for t in range(5):
        model = models_list[t]
        goods = goods_list[t]
        count = faker.random.randint(5, 51)
        price_count = prices_list[t]
        id_price = id_prices[t]
        clients = Client(model, goods, count, price_count, id_price)
        session.add(clients)
    session.commit()

    for i in range(5):
        clients = faker.random.choice(client_list)
        count1 = faker.random.randint(1, 5)
        id_price = faker.random.choice(id_prices)
        firm = Firm(id_price, count1, clients)
        session.add(firm)
    session.commit()
    session.close()
