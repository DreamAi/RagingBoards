import zipfile
import os

def create_zip():

    with zipfile.ZipFile("raging_boards_release.zip","w") as z:

        for root,dirs,files in os.walk("."):

            for f in files:
                z.write(os.path.join(root,f))
