import os
import subprocess
import platform

PROJECT = "RagingBoards"

def run(cmd):
    print(cmd)
    subprocess.call(cmd, shell=True)

def create(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path,"w") as f:
        f.write(content)

def install_dependencies():

    run("pip install fastapi uvicorn numpy tensorflow reportlab psutil")

def create_wave_ai():

    create("ai/wave_ai.py",""" 
import numpy as np

class WaveAI:

    def predict_wave_energy(self, height, period):

        energy = 0.5 * height**2 * period

        return energy
""")

def create_performance_ai():

    create("ai/performance_ai.py","""
import numpy as np

class PerformanceAI:

    def score(self,length,width,rocker):

        speed = length / (rocker+0.01)

        control = width * 0.5

        return (speed + control)/2
""")

def create_wave_physics():

    create("simulation/wave_physics.py","""
import numpy as np

class WaveSimulation:

    def simulate(self,height,period):

        velocity = (height * period)**0.5

        return velocity
""")

def create_board_dynamics():

    create("simulation/board_dynamics.py","""
class BoardDynamics:

    def drag(self,length,width):

        return length * width * 0.08
""")

def create_marketplace():

    create("marketplace/marketplace_api.py","""
from fastapi import FastAPI

app = FastAPI()

boards = []

@app.post("/list_board")
def list_board(data:dict):

    boards.append(data)

    return {"status":"listed"}

@app.get("/boards")

def get_boards():

    return boards
""")

def create_ar_viewer():

    create("mobile_ar/ar_viewer.js","""
import * as THREE from 'three'

export function ARBoard(){

    const geometry = new THREE.CylinderGeometry(0.3,0.2,2,64)

    const material = new THREE.MeshStandardMaterial({color:0xffffff})

    const board = new THREE.Mesh(geometry,material)

    return board
}
""")

def create_backend():

    create("backend/main_api.py","""
from fastapi import FastAPI
from ai.wave_ai import WaveAI
from ai.performance_ai import PerformanceAI

app = FastAPI()

wave = WaveAI()
perf = PerformanceAI()

@app.get("/predict_wave")

def predict(height:float,period:float):

    return {"energy":wave.predict_wave_energy(height,period)}

@app.get("/board_score")

def score(length:float,width:float,rocker:float):

    return {"score":perf.score(length,width,rocker)}
""")

def create_frontend():

    create("frontend/studio.jsx","""
import React from 'react'

export default function Studio(){

return(

<div>

<h1>Raging Boards Studio</h1>

</div>

)

}
""")

def create_ai_agents():

    create("ai/telemetry_ai.py","""
class TelemetryAI:

    def analyze(self,data):

        avg_speed = sum(data)/len(data)

        return avg_speed
""")

def create_self_heal():

    create("ai/self_heal.py","""
import psutil
import time
import os

while True:

    if not any('uvicorn' in p.name() for p in psutil.process_iter()):

        os.system('uvicorn backend.main_api:app --reload &')

    time.sleep(20)
""")

def create_run_script():

    create("run_platform.py","""
import os

os.system("uvicorn backend.main_api:app --reload")
""")

def main():

    os.makedirs(PROJECT,exist_ok=True)

    os.chdir(PROJECT)

    install_dependencies()

    create_wave_ai()

    create_performance_ai()

    create_wave_physics()

    create_board_dynamics()

    create_marketplace()

    create_ar_viewer()

    create_backend()

    create_frontend()

    create_ai_agents()

    create_self_heal()

    create_run_script()

    print("Raging Boards V3 Installed")

if __name__ == "__main__":

    main()
