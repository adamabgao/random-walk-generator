# Random Walk Generator

## Overview
This is a simple Python project that generates and visualizes a **random walk** using Matplotlib.  
A random walk is a stochastic process that involves a series of **sequentially-ordered random movements**, similar to a **drunken walk** or **Brownian motion**.

### **Dependencies**
Ensure you have the required library installed:
```sh
pip install matplotlib
```
- **matplotlib**: Used for plotting the random walk.

---

## Usage
Run `main.py` to generate and display a random walk visualization.

### **Example Usage**
```python
from rwgenerator import RWGenerator

# Generate and display a random walk with 5,000 steps
RWGenerator(num_steps=5_000).scatter(dot_size=5)

# Generate and save a random walk with 50,000 steps
RWGenerator(num_steps=50_000).scatter(dot_size=5, savefig=True)
```
- `num_steps`: Specifies the number of steps in the random walk.
- `dot_size`: Controls the size of scatterplot points.
- `savefig`: If `True`, saves the plot as `"rw_plot.png"`.

---

## **Reference**
| Class       | Type           | Method/Function | Description                                                             |
| ----------- | -------------- | --------------- | ----------------------------------------------------------------------- |
| `RandomWalk`  | Class           | `__init__()`        | Initializes a random walk object with `num_steps`. |
| `RandomWalk`  | Helper Method   | `go_for_walk()`  | Generates random walk coordinates. |
| `RandomWalk`  | Helper Method   | `random_steps()` | Produces a random step in x and y directions. |
| `RWGenerator` | Class           | `__init__()`      | A generator class for random walk objects that creates different plots. |
| `RWGenerator` | Method          | `scatter()`      | Creates a **scatterplot** representation of the random walk. |

---

### **RWGenerator Class**
#### **`__init__(self, num_steps=5000)`**
- Initializes `RWGenerator` and creates an instance of `RandomWalk`.
- **Attributes**:
  - `num_steps`: Number of steps in the walk (default: `5000`).

#### **`scatter(self, dot_size=10, savefig=False)`**
- Generates and visualizes the **random walk** using `matplotlib`.
- **Parameters**:
  - `dot_size (int)`: Controls scatterplot point size (default: `10`).
  - `savefig (bool)`: If `True`, saves the graph as `rw_plot.png`. Default is `False`.

# Example Output
`RWGenerator(num_steps=15).scatter(dot_size=100_000, savefig= True)`
![image](https://github.com/user-attachments/assets/2b8f9a26-3ea0-4e14-a02e-6d43cb608e2c)

`RWGenerator(num_steps=15).scatter(dot_size=200, savefig= True)`
![image](https://github.com/user-attachments/assets/b5216bb8-51d4-4c25-a82f-a5f488bdb9c9)

---

## License
This project is open-source and licensed under the **MIT License**.

---
