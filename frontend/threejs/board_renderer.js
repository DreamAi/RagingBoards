import * as THREE from "three";

export function createSurfboard(scene) {

    const geometry = new THREE.CylinderGeometry(
        0.25,
        0.3,
        2.0,
        64
    );

    const texture = new THREE.TextureLoader().load(
        "/textures/surfboard_graphic.png"
    );

    const material = new THREE.MeshStandardMaterial({
        map: texture,
        metalness: 0.3,
        roughness: 0.2
    });

    const board = new THREE.Mesh(geometry, material);

    board.rotation.z = Math.PI / 2;

    scene.add(board);

}
