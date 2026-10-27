# Projectile Motion Simulator

My first computational physics project, built using Python, NumPy, and Matplotlib.

## Overview

This project simulates the trajectory of a soccer ball launched from the ground at an angle of 45° with an initial speed of 20 m/s. It plots the ball's path and identifies its highest point.

The project started with a basic projectile motion problem and was extended into a numerical simulation with a visual representation of the trajectory.

## Original Problem

A soccer ball is kicked from the ground with an initial speed of 20 m/s at an angle of 45° above the horizontal, subject to gravitational acceleration of 9.8 m/s². Find the highest point the ball reaches.

## Physics

The initial velocity is resolved into horizontal and vertical components:

- Horizontal velocity: `ux = v0 * cos(theta)`
- Vertical velocity: `uy = v0 * sin(theta)`

The position of the projectile is calculated using:

- Horizontal displacement: `x = ux * t`
- Vertical displacement: `y = uy * t - 0.5 * g * t²`

The total flight time, assuming the ball lands at its launch height, is:

`t_f = 2 * uy / g`

The highest point is found numerically by locating the maximum value in the array of calculated vertical positions using NumPy's `argmax()` function.

## Results

- Initial speed: 20 m/s
- Launch angle: 45°
- Gravitational acceleration: 9.8 m/s²
- Theoretical maximum height: approximately 10.20 m
- Simulated maximum height: approximately 10.20 m

The numerical result agrees with the theoretical solution, within the precision of the simulation.

## Features

- Calculates the horizontal and vertical components of the initial velocity.
- Generates time values using NumPy.
- Computes the projectile's horizontal and vertical positions.
- Plots the trajectory using Matplotlib.
- Identifies and marks the highest point.
- Annotates the graph with the coordinates of the maximum height.

## Requirements

- Python 3
- NumPy
- Matplotlib

## How to Run

Install the required libraries:

```bash
pip install numpy matplotlib
```

Run the program:

```bash
python projectile_motion.py
```

## What I Learned

- Applying equations of motion in Python.
- Using NumPy for numerical calculations and array operations.
- Using Matplotlib to visualize physical phenomena.
- Finding maximum values in numerical data.
- Comparing numerical results with analytical solutions.

---

*This is my first step toward exploring computational physics through Python programming.*
