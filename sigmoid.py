import numpy as np
import matplotlib.pyplot as plt
def sigmoid(s):
    return 1/(1+np.exp(-s))

x_axis = np.linspace(-6,6,200)

y_axis = sigmoid(x_axis)

plt.figure(figsize=(8,4))
plt.plot (x_axis, y_axis, color = "blue", linewidth=2, label=sigmoid)
plt.title("sourabh ka banaya hua sigmoid graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid("True")
plt.show()
plt.close()