import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq

fs = 1000
t = np.linspace(0, 3, 3 * fs)
N = len(t)

noise = 0.2 * np.random.normal(0, 1, N)
signal = (1.0 * np.sin(2 * np.pi * 5 * t) + 
          0.4 * np.sin(2 * np.pi * 60 * t) + 
          noise)

F = fft(signal)
freqs = fftfreq(N, d=1/fs)

mask = freqs > 0
power = (2.0 / N) * np.abs(F[mask])
freqs_pos = freqs[mask]

F_clean = F.copy()
F_clean[np.abs(np.abs(freqs) - 60) < 2] = 0 
clean_signal = ifft(F_clean).real            


fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))


ax1.plot(t, signal, 'b')
ax1.set_xlim(0, 0.5)
ax1.set_title('Original Signal (with 60 Hz noise)')


ax2.plot(freqs_pos, power, 'k')
ax2.set_xlim(0, 80) 
ax2.set_title('Power Spectrum (Labeled Peaks)')


ax3.plot(t, clean_signal, 'r')
ax3.set_xlim(0, 0.5)
ax3.set_title('Filtered Signal (60 Hz Removed)')

fig.tight_layout()

plt.show()