import sqlalchemy
import cx_Oracle

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker

import time

if __name__ == "__main__":
    sqlalchemy.__version__
    engine =  create_engine('oracle://Trainee1:!QAZSE4@localhost', echo = False)
    connection = cx_Oracle.connect('Trainee1/!QAZSE4@localhost/xe')

    Base = declarative_base()
    cur = connection.cursor()
    result = cur.execute("Select * FROM Book")
    for row in result:
        print(row)

    class book(Base):
        __tablename__ = "BOOK"
        author = Column(String(50))
        title = Column(String(50))
        ISBN = Column(String(50), nullable=False , primary_key= True)
        price = Column(Numeric)
        numpages = Column(Numeric)
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    session = Session()
    b = book(author="Creilly", title="Advanced python", ISBN="7277py", price = 456.00, numpages = 215)
    session.add(b)
    session.commit()

    print(session.query(book).all())
    for tit in session.query(book.title).order_by(book.author):
        print(tit)
    for aut in session.query(book.author).order_by(book.title):
        print(aut)

    toupdate = session.query(book).filter(book.title =="Advanced python").first()
    toupdate.price = toupdate.price + 5
    session.commit()    