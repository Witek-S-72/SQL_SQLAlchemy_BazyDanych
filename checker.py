from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, create_engine, DateTime, desc, Numeric
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import Orders
from faker import Faker

Session = sessionmaker(bind=Orders.engine)
session = Session()

user = Orders.User(1, 'Wit', 'Sub', 'wit@sub.com', '123 Allee',)
session.add(user)

session.commit()







