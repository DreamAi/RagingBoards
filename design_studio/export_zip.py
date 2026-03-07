import zipfile

def create_zip(design_files):

    zipname = "board_design.zip"

    with zipfile.ZipFile(zipname,"w") as z:

        for f in design_files:

            z.write(f)

    return zipname
