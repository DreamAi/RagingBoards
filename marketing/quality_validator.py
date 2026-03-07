def check_quality(text):

    if len(text) < 40:

        return False

    if "best ever" in text.lower():

        return False

    if "guaranteed" in text.lower():

        return False

    return True
