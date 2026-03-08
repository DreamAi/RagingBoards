WAYNE = 0.40
BUSINESS = 0.40
SAVINGS = 0.20

def allocate(amount):

    wayne = amount * WAYNE
    business = amount * BUSINESS
    savings = amount * SAVINGS

    return {

        "wayne_capitec_account":wayne,
        "business_account":business,
        "savings_account":savings

    }
