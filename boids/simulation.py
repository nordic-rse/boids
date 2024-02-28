import pygame
from pygame.locals import *
import random
from .boid import Boid
from .functions import (
    fly_towards_center,
    avoid_others,
    match_velocity,
    limit_speed,
    keep_within_bounds,
)


def run_simulation(
    num_boids=100,
    visual_range=75,
    alignment=0.05,
    min_distance=20,
    separation=0.05,
    cohesion=0.01,
    max_speed=5,
    turning_speed=1,
    margin_between_boids=20,
    width=800,
    height=600,
):
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    boids = [
        Boid(
            x=random.uniform(0, width),
            y=random.uniform(0, height),
            dx=random.uniform(-max_speed, max_speed),
            dy=random.uniform(-max_speed, max_speed),
        )
        for _ in range(num_boids)
    ]

    gameOn = True
    while gameOn:
        screen.fill((255, 255, 255))  # Fill the screen with white background

        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Backspace key has been pressed set
                # running to false to exit the main loop
                if event.key == K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    gameOn = False

            elif event.type == QUIT:
                gameOn = False

        for boid in boids:
            fly_towards_center(
                boids, boid, visual_range=visual_range, cohesion=cohesion
            )
            avoid_others(boids, boid, min_distance=min_distance, separation=separation)
            match_velocity(boids, boid, alignment=alignment, visual_range=visual_range)
            limit_speed(boid, max_speed=max_speed)
            keep_within_bounds(
                boid,
                width=width,
                height=height,
                margin_between_boids=margin_between_boids,
                turning_speed=turning_speed,
            )
            boid.update()

        for boid in boids:
            boid.draw(screen)

        pygame.display.flip()
    pygame.quit()
