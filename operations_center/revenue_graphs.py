from finance.revenue_allocator import allocate

orders = [

100,
150,
200,
50,
300

]

def revenue_data():

    total = sum(orders)

    allocation = allocate(total)

    return {

        "total_revenue": total,
        "allocation": allocation

    }
