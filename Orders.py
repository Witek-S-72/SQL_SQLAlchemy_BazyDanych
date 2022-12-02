from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, create_engine, DateTime, desc, Numeric
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

engine = create_engine("mysql+pymysql://testy:witek_22@localhost:3306/BookShop")

class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, auto_increment=True, primary_key = True)
    user_f_name = Column(String(20), nullable = False)
    user_l_name = Column(String(50), nullable = False)
    user_email = Column(String(255), nullable = False)
    user_address = Column(String(255))
    reg_date = Column(DateTime, default=datetime.now())

    # def __repr__(self):
    #     return f'User details:' \
    #            f' id: {self.id_user}' \
    #            f'first name: {self.user_f_name}' \
    #            f'last name: {self.user_l_name}' \
    #            f'email: {self.user_email}'


class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, auto_increment=True, primary_key=True)
    book_title = Column(String(255), nullable=False)
    book_author = Column(String(255), nullable=False)

    def __repr__(self):
        return f'Book details:' \
               f' id: {self.id_book}' \
               f'title: {self.book_title}' \
               f'author: {self.book_author}' \


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, auto_increment=True, primary_key=True)
    user_id = Column(Integer)
    order_date = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    def __repr__(self):
        return f'Order details:' \
               f' id: {self.order_id}' \
               f'user: {self.user_id}' \
               f'date: {self.order_date}' \

Base.metadata.create_all(engine)