orders = []

def create_order(product, price):

    order = {

        "product": product,
        "price": price

    }

    orders.append(order)

    return order

def get_orders():

    return orders
