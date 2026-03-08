TAX_RATES = {

    "South Africa":0.15,
    "USA":0.07,
    "UK":0.20,
    "EU":0.21

}

def calculate_tax(country,amount):

    rate = TAX_RATES.get(country,0.15)

    tax = amount * rate

    return amount + tax
