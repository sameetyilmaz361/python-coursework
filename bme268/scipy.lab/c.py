import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq

fs = 500
t = np.linspace(0,2, fs*2)

signal = 1.0 * np.sin(2*np.pi*1.2*t) + 0.3 * np.sin(2*np.pi*40*t) + 0.5 * np.sin(2*np.pi*50*t)

N = len(t)
F = fft(signal)
freqs = fftfreq(N,d=1/fs)

mask = freqs > 0
power = (2.0/N) * np.abs(F[mask])
freqs_pos= freqs[mask]

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(freqs_pos, power, 'b-', lw=2)
ax.set_xlim(0, 80)
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude')
ax.set_title('Frequency Spectrum of the Signal')

plt.show()

