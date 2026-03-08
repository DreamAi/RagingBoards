from reportlab.pdfgen import canvas

def create_board_pdf(board):

    c = canvas.Canvas("board_design.pdf")

    c.drawString(100,750,"Raging Boards Design")

    c.drawString(100,720,str(board))

    c.save()
