
import random
import string

from faker import Faker
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, create_engine, DateTime, desc, Numeric
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("mysql+pymysql://root:witek_22@localhost:3306/Parts")


class Parts(Base):
    __tablename__ = 'part_selling'

    part_id = Column(Integer, primary_key=True)
    part_name = Column(String(50), nullable=False)
    date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    my_price = Column(Numeric(7,2))

    def __init__(self, part_id, part_name, date, my_price):
        self.part_id = part_id
        self.part_name = part_name
        self.date = datetime.now()
        self.my_price = my_price


    def __repr__(self):
        return f'Parts details:' \
               f' id: {self.part_id}' \
               f'part name: {self.part_name}' \
               f'item: {self.date}' \
               f'part price: {self.my_price}'

Base.metadata.create_all(engine)





