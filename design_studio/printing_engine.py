paid_users = []

def allow_print(user):

    return user in paid_users

def print_design(user, design):

    if not allow_print(user):

        return "Upgrade required"

    return "Sending design to printer"
