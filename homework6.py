import numpy as np
import matplotlib.pyplot as plt

# Define system parameters
L = 1  # inductance
R = 1  # resistance
wo = 1  # fundamental frequency
duty_cycle = 0.1  # duty cycle of input square wave

# Define input waveform
T = 2 * np.pi / wo
t = np.linspace(0, T, 1000)
x = 0.5 * np.sign(np.sin(wo * t)) + 0.5

# Compute Fourier series coefficients
N = 50
c = np.zeros(N, dtype=np.complex128)
for n in range(1, N + 1):
    An = (4 / np.pi) * np.sin(n * np.pi / 10)
    if n % 2 == 0:
        phin = 0
    else:
        phin = -np.pi / 2
    c[n-1] = (1 / T) * np.sum(x * np.exp(-1j * n * wo * t + 1j * phin)) * (2 * np.pi / wo)

# Compute N-term approximation of output waveform
yN = np.zeros_like(t, dtype=np.complex128)
for n in range(1, N + 1):
    yN += c[n-1] * np.exp(1j * n * wo * t)

# Plot input and N-term approximation of output
plt.plot(t, x, linewidth=2)
plt.plot(t, yN.real, linewidth=2)
plt.xlim([0, T])
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend(['Input', 'Output (N=50)'])
plt.show()
