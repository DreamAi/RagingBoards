from fastapi import FastAPI
from cart_api import add_to_cart, get_cart
from order_api import create_order, get_orders
from dashboard_api import revenue_summary

app = FastAPI()

@app.get("/")
def root():

    return {"platform":"Raging Boards Store"}

@app.post("/cart")

def cart_add(item:dict):

    return add_to_cart(item)

@app.get("/cart")

def cart():

    return get_cart()

@app.post("/order")

def order(product:str, price:float):

    return create_order(product,price)

@app.get("/orders")

def orders():

    return get_orders()

@app.get("/dashboard/revenue")

def dashboard():

    return revenue_summary()
