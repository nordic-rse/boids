"""Example python package for boids simulation"""

__version__ = "0.2.1"

from .boid import Boid
from .simulation import run_simulation
from .functions import (
    keep_within_bounds,
    fly_towards_center,
    avoid_others,
    match_velocity,
    limit_speed,
)
