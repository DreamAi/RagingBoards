allowed_claims = [

"AI design tools",
"surfboard graphics design",
"surfboard visualization",
"design export for builders"

]

def validate(text):

    for claim in allowed_claims:

        if claim in text.lower():

            return True

    return False
