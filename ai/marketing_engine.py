platforms = [
"instagram",
"linkedin",
"tiktok"
]

def create_post():

    return "Design your custom surfboard with Raging Boards."

def publish():

    post = create_post()

    for p in platforms:
        print("Posting to",p)
