import matplotlib.pyplot as plt
import numpy as np 
import math



x = np.linspace(-10,10, 100)
x_one_wave =  np.linspace(-np.pi, np.pi, 200)

y = np.linspace(-10,10, 100)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_log = np.log (x)
y_exp = np.exp(x)
y_power = np.power(x,2)



# plt.plot(x,y_power)
# plt.plot(x,y_sin)
# plt.plot(x,y_cos)
# plt.plot(x,y_log)
# plt.plot(x,y_exp)

plt.plot(x,y)


plt.axis([-10,10,-10,10]) 
plt.show()
