import pygame
from pygame.locals import *
import random
from dataclasses import dataclass, field
import numpy as np


@dataclass
class Boid:
    x: float
    y: float
    dx: float
    dy: float

    def update(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.x), int(self.y)), 2)



def distance(boid1, boid2):
    return np.sqrt((boid1.x - boid2.x) ** 2 + (boid1.y - boid2.y) ** 2)


def keep_within_bounds(boid, width=800, height=600, margin=20, turn_factor=1):
    if boid.x < margin:
        boid.dx += turn_factor
    elif boid.x > width - margin:
        boid.dx -= turn_factor

    if boid.y < margin:
        boid.dy += turn_factor
    elif boid.y > height - margin:
        boid.dy -= turn_factor


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


def avoid_others(boids, boid, min_distance=20, avoid_factor=0.05):
    move_x, move_y = 0, 0

    for other_boid in boids:
        if other_boid is not boid:
            if distance(boid, other_boid) < min_distance:
                move_x += boid.x - other_boid.x
                move_y += boid.y - other_boid.y

    boid.dx += move_x * avoid_factor
    boid.dy += move_y * avoid_factor


def match_velocity(boids, boid, matching_factor=0.05, visual_range=100):
    avg_dx, avg_dy, num_neighbors = 0, 0, 0

    for other_boid in boids:
        if distance(boid, other_boid) < visual_range:
            avg_dx += other_boid.dx
            avg_dy += other_boid.dy
            num_neighbors += 1

    if num_neighbors:
        avg_dx /= num_neighbors
        avg_dy /= num_neighbors
        boid.dx += (avg_dx - boid.dx) * matching_factor
        boid.dy += (avg_dy - boid.dy) * matching_factor


def limit_speed(boid, max_speed=10):
    speed = np.sqrt(boid.dx ** 2 + boid.dy ** 2)
    if speed > max_speed:
        boid.dx = (boid.dx / speed) * max_speed
        boid.dy = (boid.dy / speed) * max_speed


def main():
    # Boid simulation parameters
    num_boids = 100
    visual_range = 75
    max_speed = 5
    turn_factor = 1
    margin = 20

    width, height = 800, 600

    # initialize pygame
    pygame.init()
    
    # # Define the dimensions of screen object
    screen = pygame.display.set_mode((width, height))

    boids = [Boid(x=random.uniform(0, width),
                y=random.uniform(0, height),
                dx=random.uniform(-max_speed, max_speed),
                dy=random.uniform(-max_speed, max_speed))
            for _ in range(num_boids)]

    gameOn = True
    while gameOn:
        screen.fill((255, 255, 255))  # Fill the screen with white background

        for event in pygame.event.get():
            
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                
                # If the Backspace key has been pressed set
                # running to false to exit the main loop
                if event.key == K_BACKSPACE:
                    gameOn = False
                    
            elif event.type == QUIT:
                gameOn = False
    
        for boid in boids:
            fly_towards_center(boids, boid, visual_range=visual_range)
            avoid_others(boids, boid)
            match_velocity(boids, boid, visual_range=visual_range)
            limit_speed(boid, max_speed=max_speed)
            keep_within_bounds(boid, width=width, height= height, margin=margin, turn_factor=turn_factor)
            boid.update()

        for boid in boids:
            boid.draw(screen)

        pygame.display.flip()

import cProfile
cProfile.run('main()')