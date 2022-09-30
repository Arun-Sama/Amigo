from Model import Product
from database import Product_details, engine
from sqlalchemy.orm import Session


class Item_details:

    def insert(self, productDetails: Product):
        db = Session(engine)
        details = Product_details(name=productDetails.Title, price=productDetails.Price, summary=productDetails.Summary,
                                  id=productDetails.Id)
        db.add(details)
        db.commit()
        return productDetails

    def get_details(self, product_Id):
        db = Session(engine)
        result = db.query(Product_details).filter(Product_details.id == product_Id).all()
        mylist = []
        for i in result:
            mylist.append(i)
        return mylist


    def get_name(self,name):
        db = Session(engine)
        result = db.query(Product_details).filter(Product_details.name == name).all()
        mylist = []
        for i in result:
            mylist.append(i)
        return mylist

