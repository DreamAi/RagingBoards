VAT_RATE = 0.15

def calculate_vat(amount):

    vat = amount * VAT_RATE

    return {
        "subtotal": amount,
        "vat": vat,
        "total": amount + vat
    }
