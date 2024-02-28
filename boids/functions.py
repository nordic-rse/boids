import numpy as np


def keep_within_bounds(
    boid, width=800, height=600, margin_between_boids=20, turning_speed=1
):
    if boid.x < margin_between_boids:
        boid.dx += turning_speed
    elif boid.x > width - margin_between_boids:
        boid.dx -= turning_speed

    if boid.y < margin_between_boids:
        boid.dy += turning_speed
    elif boid.y > height - margin_between_boids:
        boid.dy -= turning_speed


def distance(boid1, boid2):
    return np.sqrt((boid1.x - boid2.x) ** 2 + (boid1.y - boid2.y) ** 2)


def fly_towards_center(boids, boid, cohesion=0.01, visual_range=100):
    centerX, centerY, num_neighbors = 0, 0, 0

    for other_boid in boids:
        if distance(boid, other_boid) < visual_range:
            centerX += other_boid.x
            centerY += other_boid.y
            num_neighbors += 1

    if num_neighbors:
        centerX /= num_neighbors
        centerY /= num_neighbors
        boid.dx += (centerX - boid.x) * cohesion
        boid.dy += (centerY - boid.y) * cohesion


def avoid_others(boids, boid, min_distance=20, separation=0.05):
    move_x, move_y = 0, 0

    for other_boid in boids:
        if other_boid is not boid:
            if distance(boid, other_boid) < min_distance:
                move_x += boid.x - other_boid.x
                move_y += boid.y - other_boid.y

    boid.dx += move_x * separation
    boid.dy += move_y * separation


def match_velocity(boids, boid, alignment=0.05, visual_range=100):
    avg_dx, avg_dy, num_neighbors = 0, 0, 0

    for other_boid in boids:
        if distance(boid, other_boid) < visual_range:
            avg_dx += other_boid.dx
            avg_dy += other_boid.dy
            num_neighbors += 1

    if num_neighbors:
        avg_dx /= num_neighbors
        avg_dy /= num_neighbors
        boid.dx += (avg_dx - boid.dx) * alignment
        boid.dy += (avg_dy - boid.dy) * alignment


def limit_speed(boid, max_speed=10):
    speed = np.sqrt(boid.dx**2 + boid.dy**2)
    if speed > max_speed:
        boid.dx = (boid.dx / speed) * max_speed
        boid.dy = (boid.dy / speed) * max_speed
