import random
import datetime
import db
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=db.engine)
session = Session()

# part_list = ['sruba','nakretka','podkladka','sprezyna','zacisk','bezpiecznik','O-ring']
#
# for i in range(1,21):
#     part_name = random.choice(part_list)
#     my_price = random.randint(10, 100)
#
#     every_part = db.Parts(i, part_name, datetime.datetime.now(), my_price)
#
#     session.add(every_part)
#
# session.commit()

if __name__ == '__main__':
    # items = session.query(db.Parts).get(5)
    # print(items)
    # session.delete(items)
    # session.commit()

    check = session.query(db.Parts.part_name)
    # print(check)
    for i in check:
        print(i)



