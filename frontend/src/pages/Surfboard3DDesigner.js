import React, {useEffect} from "react"
import * as THREE from "three"

export default function Surfboard3DDesigner(){

useEffect(()=>{

const scene = new THREE.Scene()

const camera = new THREE.PerspectiveCamera(
75,
window.innerWidth/window.innerHeight,
0.1,
1000
)

const renderer = new THREE.WebGLRenderer()
renderer.setSize(window.innerWidth,500)

document.getElementById("board3d").appendChild(renderer.domElement)

const geometry = new THREE.CylinderGeometry(0.3,0.3,4,32)
const material = new THREE.MeshStandardMaterial({color:0xffffff})

const board = new THREE.Mesh(geometry,material)

scene.add(board)

const light = new THREE.DirectionalLight(0xffffff,1)
light.position.set(2,2,5)

scene.add(light)

camera.position.z=6

function animate(){
requestAnimationFrame(animate)
board.rotation.y += 0.01
renderer.render(scene,camera)
}

animate()

},[])

return <div id="board3d"></div>

}
