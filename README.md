# boids

Example python package simulating boids: https://en.wikipedia.org/wiki/Boids. This package serves as an example for researchers on how to turn their python code into a package.

<img src="https://github.com/gregordecristoforo/boids/blob/main/readme_assets/boids.gif" alt="Boids evolution" width="500" />


## Installation
The package is published to PyPI and can be installed with
```sh
pip install boids
```

If you want the development version you must first clone the repo to your local machine,
then install the project in development mode:

```sh
git clone https://github.com/gregordecristoforo/boids.git
cd boids
python -m pip install -e .
```

## Usage
Import and run the `run_simulation()` function:
```Python
import boids

boids.run_simulation()
```

You can overrite the default arguments as you wish (see the [`run_simulations()` docstring](https://github.com/gregordecristoforo/boids/blob/main/boids/simulation.py) for a list of all input arguments):
```Python
boids.run_simulation(num_boids=50, alignment=0.03, separation=0.03, cohesion=0.02)
```

## Reproducibility
In order to guarantee that this project remains reproducible we include a `environment.yml` file specifying the exact version of all dependencies. Recreate a conda environment with these packages by:
```sh
conda env create -f environment.yml
``` 
