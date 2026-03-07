orders = [

"Custom board design",
"Graphic pack",
"Performance template"

]

def marketplace_stats():

    return {

        "recent_orders": orders,
        "orders_today": len(orders)

    }
