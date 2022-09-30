from fastapi import FastAPI
from Model import Product
from code import Item_details
import uvicorn

app = FastAPI()

item = Item_details()


@app.post('/')
def insert_products(productDetails: Product):
    result = item.insert(productDetails)
    return result


@app.get('/')
def get_products(product_Id):
    result = item.get_details(product_Id)
    return result


@app.get('/name')
def get_details(name):
    result = item.get_name(name)
    return result

