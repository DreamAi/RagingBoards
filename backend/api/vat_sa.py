VAT_RATE = 0.15

def calculate_vat(amount):

    vat = amount * VAT_RATE
    total = amount + vat

    return {
        "subtotal":amount,
        "vat":vat,
        "total":total
    }
