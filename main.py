import numpy as np
import plotly.graph_objects as go
import json
import os

# Gravitational constant
G = 6.67430e-11  
M_sun = 1.989e30  # Mass of the Sun in kg

# Load real orbital elements from JSON
def load_orbital_elements():
    with open("orbital_elements.json", "r") as f:
        return json.load(f)

def compute_initial_conditions(elements):
    """ Compute planetary positions and velocities from Keplerian elements. """
    planets = []
    for name, data in elements.items():
        a = data["semi_major_axis"]
        e = data["eccentricity"]
        T = np.sqrt((4 * np.pi**2 * a**3) / (G * M_sun))

        # Assume starting at perihelion
        r = a * (1 - e)
        velocity = np.sqrt(G * M_sun * ((2 / r) - (1 / a)))

        planets.append(Planet(name, data["mass"], [r, 0, 0], [0, velocity, 0]))
    return planets

class Planet:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.force = np.array([0.0, 0.0, 0.0], dtype=float)

def compute_forces(planets):
    """ Compute gravitational forces using vectorized NumPy operations. """
    positions = np.array([p.position for p in planets])
    masses = np.array([p.mass for p in planets]).reshape(-1, 1)

    deltas = positions[:, np.newaxis, :] - positions[np.newaxis, :, :]
    distances = np.linalg.norm(deltas, axis=2) + np.eye(len(planets))
    forces = G * masses * masses.T / distances**2
    forces[np.eye(len(planets), dtype=bool)] = 0

    for i, planet in enumerate(planets):
        planet.force = np.sum(forces[:, i][:, np.newaxis] * deltas[:, i, :] / distances[:, i][:, np.newaxis], axis=0)

def rk4_update(planets, dt):
    """ Perform one step of the Runge-Kutta 4th order integration. """
    for planet in planets:
        pos0, vel0, mass = planet.position, planet.velocity, planet.mass

        compute_forces(planets)
        a0 = planet.force / mass

        k1_v = a0 * dt
        k1_r = vel0 * dt

        k2_v = (planet.force / mass) * dt
        k2_r = (vel0 + k1_v / 2) * dt

        k3_v = (planet.force / mass) * dt
        k3_r = (vel0 + k2_v / 2) * dt

        k4_v = (planet.force / mass) * dt
        k4_r = (vel0 + k3_v) * dt

        planet.velocity += (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
        planet.position += (k1_r + 2 * k2_r + 2 * k3_r + k4_r) / 6

def simulate(planets, num_steps, dt):
    """ Run the full simulation and store positions. """
    all_positions = {p.name: [] for p in planets}
    for step in range(num_steps):
        rk4_update(planets, dt)
        for p in planets:
            all_positions[p.name].append(p.position.copy())
    return all_positions

def save_simulation(positions, filename="simulation.npz"):
    """ Save simulation results for future use. """
    np.savez(filename, **positions)

def load_simulation(filename="simulation.npz"):
    """ Load previous simulation results. """
    data = np.load(filename, allow_pickle=True)
    return {key: data[key] for key in data.keys()}

def plot_simulation(positions):
    """ Generate a 3D plot using Plotly. """
    fig = go.Figure()
    for name, pos in positions.items():
        pos_array = np.array(pos)
        fig.add_trace(go.Scatter3d(x=pos_array[:, 0], y=pos_array[:, 1], z=pos_array[:, 2], mode='lines', name=name))
    fig.update_layout(title="Solar System Simulation (3D)", scene=dict(xaxis_title="X (m)", yaxis_title="Y (m)", zaxis_title="Z (m)"))
    fig.show()

if __name__ == "__main__":
    elements = load_orbital_elements()
    planets = compute_initial_conditions(elements)

    num_steps = int(input("Enter number of simulation steps (e.g., 1000): "))
    dt = float(input("Enter time step in seconds (e.g., 86400 for 1 day): "))

    positions = simulate(planets, num_steps, dt)
    save_simulation(positions)
    plot_simulation(positions)
