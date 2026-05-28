import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0,x)

def relu_derivative(x):
    return (x>0).astype(float)

x = np.linspace (-6,6,200)
fig, axes = plt.subplots(1,2)

plt.show()