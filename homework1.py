import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,1,1000) 
#x2
y = ((np.exp(1j * 2 * np.pi * t)))
plt.plot(t,np.real(y))
plt.xlabel("t")
plt.ylabel("x2(t)")
plt.show()

#x3
y = (((np.exp(1j * 2 * np.pi * t)) + (np.exp(-1j * 2 * np.pi * t)))/2)
plt.plot(t,np.real(y))
plt.xlabel("t")
plt.ylabel("x3(t)")
plt.show()