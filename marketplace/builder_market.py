from fastapi import FastAPI

app = FastAPI()

builders = []
boards = []

@app.post("/builder")

def add_builder(data:dict):

    builders.append(data)

    return {"status":"builder added"}

@app.post("/board")

def list_board(data:dict):

    boards.append(data)

    return {"status":"board listed"}

@app.get("/boards")

def get_boards():

    return boards
