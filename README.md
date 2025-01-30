# 🌍 Solar System Simulation
**A Python-based solar system simulator using real NASA orbital elements, Runge-Kutta integration, and 3D visualization with Plotly.**

![Simulation Screenshot](simulation_preview.png)  
(*If you don’t have an image yet, take a screenshot of your simulation and add it to the repo!*)

---

## 📜 Features
✅ Uses real NASA orbital elements to calculate planetary positions  
✅ Implements **Runge-Kutta (RK4)** for accurate orbit simulation  
✅ 3D visualization with **Plotly**  
✅ Fast computation with **NumPy vectorization**  
✅ Supports saving and loading simulations  

---

## ⚙️ Installation
Make sure you have **Python 3.8+** installed. Then, clone this repository and install the dependencies:

```sh
git clone https://github.com/your-username/solar-system-simulation.git
cd solar-system-simulation
pip install -r requirements.txt
```

---

## 🚀 How to Run
Run the simulation with:

```sh
python simulation.py
```

You'll be prompted to enter the number of simulation steps and time step:

```
Enter number of simulation steps (e.g., 1000): 1000
Enter time step in seconds (e.g., 86400 for 1 day): 86400
```

After running, a **3D visualization** will appear showing the planetary orbits.

---

## 📊 Saving & Loading Simulations
You can save a simulation and reload it later:

```sh
# Save a new simulation
python simulation.py --save simulation.npz

# Load and visualize a previous simulation
python simulation.py --load simulation.npz
```

---

## 🌎 Example Output
Here’s an example of what the simulation generates:

---

## 🛠️ Customization
Want to modify the planets or add custom objects? Edit **orbital_elements.json** and change the semi-major axis, eccentricity, or mass to include asteroids, moons, or exoplanets!

---

## 📜 Future Improvements
- 🌠 **Real-time animation** instead of precomputed paths  
- 🚀 **Custom object insertion** (add spacecraft, asteroids, etc.)  
- 🪐 **Moon systems** (simulate moons of Jupiter, Saturn, etc.)  

---

## 📝 Acknowledgments
🌌 **Data Sources:** NASA JPL Horizons System  
📚 **Algorithms:** Runge-Kutta 4th Order, Keplerian orbital mechanics  

---

## 📜 License
This project is licensed under the MIT License.

-
