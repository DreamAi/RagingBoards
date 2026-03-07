banned_words = [
"guaranteed",
"perfect performance",
"miracle",
"instant pro surfer"
]

def validate(content):

    for word in banned_words:
        if word in content.lower():
            return False

    return True
