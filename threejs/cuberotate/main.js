import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
);
camera.position.z = 5;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Utility to create 6-colored cube
function createColorfulCube(colors) {
  const materials = colors.map(color => new THREE.MeshBasicMaterial({ color }));
  const geometry = new THREE.BoxGeometry(1, 1, 1);
  return new THREE.Mesh(geometry, materials);
}

// Define 3 sets of 6 colors
const colorSets = [
  [0xff0000, 0x00ff00, 0x0000ff, 0xffff00, 0xff00ff, 0x00ffff], // Red-Green-Blue-Yellow-Magenta-Cyan
  [0x8b0000, 0x006400, 0x00008b, 0xffa500, 0x800080, 0x4682b4], // Darker tones
  [0xff69b4, 0x7fff00, 0x1e90ff, 0xffd700, 0xdda0dd, 0x40e0d0]  // Pastel vibes
];

// Create cubes
const cubes = colorSets.map((colors, i) => {
  const cube = createColorfulCube(colors);
  cube.position.set(i * 2 - 2, i % 2 === 0 ? 1.5 : -1.5, 0);
  scene.add(cube);
  return cube;
});

// Velocities
const velocities = [
  new THREE.Vector3(0.02, 0.015, 0),
  new THREE.Vector3(-0.015, 0.02, 0),
  new THREE.Vector3(0.017, -0.017, 0)
];

// Scene bounds
const bounds = {
  x: camera.position.z * Math.tan((camera.fov * Math.PI) / 360) * camera.aspect,
  y: camera.position.z * Math.tan((camera.fov * Math.PI) / 360)
};

// Collision detection
function checkCollision(boxA, boxB) {
  return boxA.intersectsBox(boxB);
}

function animate() {
  requestAnimationFrame(animate);

  for (let i = 0; i < cubes.length; i++) {
    const cube = cubes[i];
    cube.position.add(velocities[i]);

    // Edge bounce
    const box = new THREE.Box3().setFromObject(cube);
    if (box.max.x > bounds.x || box.min.x < -bounds.x) velocities[i].x *= -1;
    if (box.max.y > bounds.y || box.min.y < -bounds.y) velocities[i].y *= -1;

    // Cube-to-cube bounce
    for (let j = i + 1; j < cubes.length; j++) {
      const otherCube = cubes[j];
      const boxA = new THREE.Box3().setFromObject(cube);
      const boxB = new THREE.Box3().setFromObject(otherCube);

      if (checkCollision(boxA, boxB)) {
        velocities[i].x *= -1;
        velocities[i].y *= -1;
        velocities[j].x *= -1;
        velocities[j].y *= -1;
      }
    }

    // Optional: rotate for flair
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
  }

  renderer.render(scene, camera);
}

animate();