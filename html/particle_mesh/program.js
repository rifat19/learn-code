// 1. Get the canvas and its drawing contextual
const canvas = document.getElementById("meshCanvas");
const ctx = canvas.getContext("2d");

// 2. Set canvas size to full screen
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// 3. Number of particles (dots)
const numParticles = 80;

// 4. Array to store all particles
const particles = [];

// 5. Generate random particles with positions and speeds
for (let i = 0; i < numParticles; i++) {
	particles.push({
		x: Math.random() * canvas.width,	// random x position
		y: Math.random() * canvas.height,	// random y position
		vx: (Math.random() - 0.5) * 1.5,	// random x speeds
		vy: (Math.random() - 0.5) * 1.5,	// random y speeds
		radius:2							// size of particle
	});
}

// 6. Funciton to draw a line between two particles it they are close enough
function drawLine(p1, p2) {
	const dist = Math.hypot(p1.x - p2.x, p1.y - p2.y); // distance formula
	
	if (dist < 120) { //if particles are within 120 pixels
		// draw transparent white line (closer = brighter)
		ctx.strokeStyle = `rgba(255,255,255,${1 - dist / 120})`;
		ctx.beginPath();
		ctx.moveTo(p1.x, p1.y);
		ctx.lineTo(p2.x, p2.y);
		ctx.stroke();
	}
}

// 7. Main update/draw function (animation loop)
function update() {
	// clear canvas each Frame
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	
	// Loop through each particle
	for (let i = 0; i < numParticles; i++) {
		const p = particles[i];
		
		// Update particle position by velocity
		p.x += p.vx;
		p.y += p.vy;
		
		// Bounce of walls
		if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
		if (p.y < 0 || p.y > canvas.height) p.vy *= -1;
		
		// Draw particle as a small white circle
		ctx.beginPath();
		ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2); // full circle
		ctx.fillStyle = "white";
		ctx.fill();
		
		//check for nearby particles and draw lines
		for (let j = i + 1; j < numParticles; j++) {
			drawLine(p, particles[j]);
		}
	}
	
	// Keep animating
	requestAnimationFrame(update);
}

// 8. Start animation
update();

// 9. Update canvas size if window is resized
window.addEventListener('resize', () => {
	canvas.width = window.innerWidth;
	canvas.height = window.innerHeight;
});