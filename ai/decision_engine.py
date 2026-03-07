restricted_actions = [

"bank_transfer",
"legal_contract",
"tax_filing",
"company_registration"

]

def approve(action):

    if action in restricted_actions:

        return "Human approval required"

    return "Approved"
