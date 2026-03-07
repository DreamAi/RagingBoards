from reportlab.pdfgen import canvas

def create_design_pdf(filename):

    c = canvas.Canvas(filename)

    c.drawString(100,750,"Raging Boards Design File")

    c.save()
