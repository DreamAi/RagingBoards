from order_api import get_orders

def revenue_summary():

    orders = get_orders()

    total = sum(o["price"] for o in orders)

    return {

        "total_orders": len(orders),
        "revenue": total

    }
