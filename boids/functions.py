import numpy as np


def keep_within_bounds(
    boid, width=800, height=600, margin_between_boids=20, turning_speed=1
):
    """
    Adjusts the boid's direction to keep it within the specified bounds.

    If the boid is too close to the edge of the bounds, its direction is adjusted
    to move it back towards the center of the bounds.

    Parameters
    ----------
    boid : Boid
        The boid to adjust.
    width : int, optional
        The width of the bounds, by default 800.
    height : int, optional
        The height of the bounds, by default 600.
    margin_between_boids : int, optional
        The minimum distance the boid should keep from the edge of the bounds, by default 20.
    turning_speed : int, optional
        The amount to adjust the boid's direction by, by default 1.

    Returns
    -------
    None
    """
    if boid.x < margin_between_boids:
        boid.dx += turning_speed
    elif boid.x > width - margin_between_boids:
        boid.dx -= turning_speed

    if boid.y < margin_between_boids:
        boid.dy += turning_speed
    elif boid.y > height - margin_between_boids:
        boid.dy -= turning_speed


def distance(boid1, boid2):
    """
    Calculates the Euclidean distance between two boids.

    Parameters
    ----------
    boid1 : Boid
        The first boid.
    boid2 : Boid
        The second boid.

    Returns
    -------
    float
        The Euclidean distance between the two boids.
    """
    return np.sqrt((boid1.x - boid2.x) ** 2 + (boid1.y - boid2.y) ** 2)


def fly_towards_center(boids, boid, cohesion=0.01, visual_range=100):
    """
    Makes a boid fly towards the center of a group of boids.

    Parameters
    ----------
    boids : list
        The group of boids.
    boid : Boid
        The boid that should fly towards the center.
    visual_range : float
        The distance within which a boid considers other boids.
    cohesion : float
        The degree to which a boid tries to stay close to other boids.

    Returns
    -------
    None
    """
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
    """
    Adjusts a boid's direction to avoid other boids that are too close.

    Parameters
    ----------
    boids : list
        The group of boids.
    boid : Boid
        The boid that should avoid others.
    min_distance : float, optional
        The minimum distance a boid tries to keep from other boids, by default 20.
    separation : float, optional
        The degree to which a boid tries to move away from other boids, by default 0.05.

    Returns
    -------
    None
    """
    move_x, move_y = 0, 0

    for other_boid in boids:
        if other_boid is not boid:
            if distance(boid, other_boid) < min_distance:
                move_x += boid.x - other_boid.x
                move_y += boid.y - other_boid.y

    boid.dx += move_x * separation
    boid.dy += move_y * separation


def match_velocity(boids, boid, alignment=0.05, visual_range=100):
    """
    Adjusts a boid's velocity to match the average velocity of nearby boids.

    Parameters
    ----------
    boids : list
        The group of boids.
    boid : Boid
        The boid that should adjust its velocity.
    alignment : float, optional
        The degree to which a boid tries to align its velocity with other boids, by default 0.05.
    visual_range : float, optional
        The distance within which a boid considers other boids for velocity matching, by default 100.

    Returns
    -------
    None
    """
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
    """
    Limits the speed of a boid.

    If the boid's speed exceeds the maximum speed, its velocity is scaled down to the maximum speed.

    Parameters
    ----------
    boid : Boid
        The boid whose speed should be limited.
    max_speed : float, optional
        The maximum speed a boid can have, by default 10.

    Returns
    -------
    None
    """
    speed = np.sqrt(boid.dx**2 + boid.dy**2)
    if speed > max_speed:
        boid.dx = (boid.dx / speed) * max_speed
        boid.dy = (boid.dy / speed) * max_speed
