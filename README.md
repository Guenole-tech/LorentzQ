# 🌀 LorentzQ: Quantum Purity Restoration Simulation

**LorentzQ** is a modular simulation framework in Python.  
It explores an approach in quantum computing: using **non-unitary Lorentz transformations** to reverse the effects of decoherence on a qubit.


## 🎯 1. Goals & Vision

In a standard quantum computer, interaction with the environment transforms a **pure state** (usable) into a **mixed state** (noisy).  

In this project, we show that by applying a *boost* (analogous to an acceleration in Minkowski space applied to the Bloch sphere), it is possible to bring the qubit’s state back toward the surface of the sphere, thereby restoring its **fidelity**.



## 🧬 2. Scientific Foundations & Calculations

The project relies on a correspondence between a qubit’s state and the geometry of Minkowski space.

### A. State Representation (Bloch Vector)

Any quantum state of a qubit is described by a density matrix $$\rho$$, decomposed in the Pauli basis $$\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$$:

$$
\rho = \frac{1}{2}(I + \vec{r} \cdot \vec{\sigma})
$$

$$
\rho =
\frac{1}{2}
\begin{pmatrix}
1 + r_z & r_x - i r_y \\
r_x + i r_y & 1 - r_z
\end{pmatrix}
$$

where $$\vec{r}$$ is the Bloch vector.

- If $$\|\vec{r}\| = 1$$ → **pure state**  
- If $$\|\vec{r}\| < 1$$ → **mixed state** (presence of noise)



### B. Decoherence Modeling (Noise)

The simulator applies a depolarizing channel at each step:

$$
\rho_{n+1} = (1 - \gamma)\rho_n + \gamma \frac{I}{2}
$$

where $$\gamma$$ is the error rate.

This transformation contracts the Bloch vector toward the origin, reducing purity $$P$$:

$$
P = \mathrm{Tr}(\rho^2) = \frac{1}{2}(1 + \|\vec{r}\|^2)
$$


### C. Lorentz Transformation (Boost)

The qubit is interpreted as a four-vector in Minkowski space.  
To restore purity, a non-unitary boost is applied:

$$
B(\eta) = \exp\left(\frac{\eta}{2} \sigma_z\right)=
\begin{pmatrix}
e^{\eta/2} & 0 \\
0 & e^{-\eta/2}
\end{pmatrix}
$$

#### Dynamic Calculation of Rapidities $$\eta$$

The correction is determined using the invariant interval $$s^2$$:

1. Component extraction:

$$
x_0 = \mathrm{Tr}(\rho I), \quad x_3 = \mathrm{Tr}(\rho \sigma_z)
$$

2. Minkowski metric:

$$
s^2 = x_0^2 - x_3^2
$$

3. Rapidities calculation:

$$
\eta = \mathrm{arctanh}(1 - s^2) \times \text{gain}
$$

(valid if $$s^2 > 0$$)


### Corrected State

The corrected state is then normalized:

$$
\rho_{LQ} =
\frac{B(\eta)\, \rho \, B(\eta)^\dagger}
{\mathrm{Tr}(B(\eta)\, \rho \, B(\eta)^\dagger)}
$$

## 📂 3. Modular Architecture

The project follows software engineering principles (**separation of concerns**).

### 🟦 I. Core Physics (physics.py)

Central linear algebra module.

- **QuantumSimulator**: manages density matrix evolution and Lorentz boosts  
- **calcul_purete(rho)**: computes quantum state purity  


### 🟩 II. Visual Interface (`visualizer.py`)

Responsible for graphical rendering.

- **LorentzVisualizer**: advanced Matplotlib configuration (dark mode, grid, dynamic annotations)  
- **FuncAnimation**: real-time animation comparing standard system vs LorentzQ  


### 🟧 III. Orchestrator (main.py)

Main entry point.

- Initializes simulation parameters  
- Automatically detects the user’s **Downloads** folder via pathlib  
- Handles video export (FFMPEG) with GIF fallback  


## 🚀 4. Quick Installation

### Required Libraries

pip install numpy matplotlib scipy
