import pytest
from .boid import Boid
from .functions import (
    fly_towards_center,
    avoid_others,
    match_velocity,
    limit_speed,
    keep_within_bounds,
)


def test_keep_within_bounds():
    # Test that a boid outside the bounds is moved back in
    boid = Boid(x=900, y=700, dx=0, dy=0)
    keep_within_bounds(boid)
    assert boid.dx < 0
    assert boid.dy < 0

    # Test that a boid near the edge of the bounds is moved away from the edge
    boid = Boid(x=790, y=590, dx=0, dy=0)
    keep_within_bounds(boid)
    assert boid.dx < 0
    assert boid.dy < 0

    # Test that a boid within the bounds is not moved
    boid = Boid(x=400, y=300, dx=0, dy=0)
    keep_within_bounds(boid)
    old_dx, old_dy = boid.dx, boid.dy
    assert boid.dx == old_dx
    assert boid.dy == old_dy


def test_fly_towards_center():
    # Test that a boid close to the other boids moves towards them
    boid = Boid(x=450, y=350, dx=0, dy=0)
    other_boids = [Boid(x=400, y=300, dx=0, dy=0), Boid(x=410, y=310, dx=0, dy=0)]
    fly_towards_center(other_boids, boid)
    assert boid.dx < 0
    assert boid.dy < 0

    # Test that a boid far from the other boids does not move
    boid = Boid(x=600, y=500, dx=0, dy=0)
    other_boids = [Boid(x=400, y=300, dx=0, dy=0), Boid(x=410, y=310, dx=0, dy=0)]
    old_dx, old_dy = boid.dx, boid.dy
    fly_towards_center(other_boids, boid)
    assert boid.dx == old_dx
    assert boid.dy == old_dy


def test_avoid_others():
    # Test that a boid near other boids moves away from them
    boid = Boid(x=410, y=310, dx=0, dy=0)
    other_boids = [Boid(x=400, y=300, dx=0, dy=0)]
    avoid_others(other_boids, boid)
    assert boid.dx > 0
    assert boid.dy > 0

    # Test that a boid far from other boids does not move
    boid = Boid(x=400, y=300, dx=0, dy=0)
    other_boids = [Boid(x=500, y=500, dx=0, dy=0)]
    old_dx, old_dy = boid.dx, boid.dy
    avoid_others(other_boids, boid)
    assert boid.dx == old_dx
    assert boid.dy == old_dy


def test_match_velocity():
    # Test that a boid near other boids gets accelarated in the same direction
    boid = Boid(x=405, y=300, dx=0, dy=0)
    other_boids = [Boid(x=400, y=300, dx=1, dy=1), Boid(x=410, y=310, dx=1, dy=1)]
    match_velocity(other_boids, boid)
    assert boid.dx > 0
    assert boid.dy > 0

    # Test that a boid far from other boids does not change its velocity
    boid = Boid(x=600, y=500, dx=0, dy=0)
    other_boids = [Boid(x=400, y=300, dx=0, dy=0), Boid(x=410, y=310, dx=0, dy=0)]
    old_dx, old_dy = boid.dx, boid.dy
    match_velocity(other_boids, boid)
    assert boid.dx == old_dx
    assert boid.dy == old_dy


def test_limit_speed():
    # Test that a boid moving too fast slows down
    boid = Boid(x=400, y=300, dx=5, dy=5)
    limit_speed(boid, max_speed=5)
    assert boid.dx < 5
    assert boid.dy < 5

    # Test that a boid moving at an acceptable speed does not change its speed
    boid = Boid(x=400, y=300, dx=5, dy=5)
    old_dx, old_dy = boid.dx, boid.dy
    limit_speed(boid, max_speed=10)
    assert boid.dx == old_dx
    assert boid.dy == old_dy
