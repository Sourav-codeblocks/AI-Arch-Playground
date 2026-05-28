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

from model import Name, Decoder, Model
#works when init file is defined

# this also works when not defined in init
from model.encoder import Name 
from model.decoder import Decoder
from model.model import Model
add_func = Name("Chaitanya")
sub_func = Decoder()
enc_dec_func = Model()

print(f"1+2={add_func.add(1, 2)}")
print(f"Name is: {add_func.get_name()}")
print(f"1-2={sub_func.sub(1, 2)}")

print(f"New model class 1+2, 1-2 = {enc_dec_func.forward(1, 2)}")