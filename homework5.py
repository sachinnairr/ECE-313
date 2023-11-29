import numpy as np
import matplotlib.pyplot as plt

w = 2*np.pi*10  
T = 2*np.pi/np.abs(w+2*np.pi)  
N1 = 10
N2 = 50

def x(t):
    return np.exp(1j*w*t)

def cn(n):
    num = np.exp(1j*(w-n*2*np.pi/T)*T)-1
    den = 1j*T*(w-n*2*np.pi/T)
    return num/den

def fourier_series(t, n):
    s = np.zeros_like(t, dtype=np.complex128)
    for i in range(-n, n+1):
        s += cn(i)*np.exp(1j*i*w*t)
    return s

t = np.linspace(0, T, 1000, endpoint=False)

plt.figure(figsize=(8, 6))
plt.plot(t, np.real(x(t)), 'b-', label='x(t)')
plt.plot(t, np.real(fourier_series(t, N1)), 'r-', label='N = %d' % N1)
plt.plot(t, np.real(fourier_series(t, N2)), 'g-', label='N = %d' % N2)
plt.xlabel('t')
plt.ylabel('Amplitude')
plt.title('Fourier Series Approximations of x(t)')
plt.legend()
plt.grid(True)

n = np.arange(-N1, N1+1)
Cn = cn(n)
plt.figure(figsize=(8, 6))
plt.stem(n, np.abs(Cn), 'b-', basefmt=' ', use_line_collection=True)
plt.xlabel('n')
plt.ylabel('|Cn|')
plt.title('Amplitude Spectrum of Fourier Coefficients (N = %d)' % N1)
plt.grid(True)

plt.figure(figsize=(8, 6))
plt.stem(n, np.angle(Cn), 'b-', basefmt=' ', use_line_collection=True)
plt.xlabel('n')
plt.ylabel('Phase [rad]')
plt.title('Phase Spectrum of Fourier Coefficients (N = %d)' % N1)
plt.grid(True)

plt.show()
