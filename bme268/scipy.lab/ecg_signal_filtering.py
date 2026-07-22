import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft, fftfreq
import os

# --- Load real ECG signal (MIT-BIH Arrhythmia Database, Lead II) ---
script_dir = os.path.dirname(os.path.abspath(__file__))
record_name = "100"

signal = np.load(os.path.join(script_dir, f"{record_name}_SIG_II.npy"))

fs = 360  # MIT-BIH standard sampling rate (Hz)
N = len(signal)
t = np.arange(N) / fs

# --- Frequency-domain analysis ---
F = fft(signal)
freqs = fftfreq(N, d=1/fs)

mask = freqs > 0
power = (2.0 / N) * np.abs(F[mask])
freqs_pos = freqs[mask]

# --- Remove 60 Hz powerline interference ---
F_clean = F.copy()
F_clean[np.abs(np.abs(freqs) - 60) < 1] = 0
clean_signal = ifft(F_clean).real

# --- Plot: show a 5-second window for readability ---
window_sec = 5
window_samples = window_sec * fs

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

ax1.plot(t[:window_samples], signal[:window_samples], 'b')
ax1.set_title(f'Raw ECG Signal (MIT-BIH record {record_name}, Lead II)')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Amplitude (mV)')

ax2.plot(freqs_pos, power, 'k')
ax2.set_xlim(0, 100)
ax2.set_title('Power Spectrum')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Power')

ax3.plot(t[:window_samples], clean_signal[:window_samples], 'r')
ax3.set_title('Filtered ECG Signal (60 Hz Removed)')
ax3.set_xlabel('Time (s)')
ax3.set_ylabel('Amplitude (mV)')

fig.tight_layout()
plt.show()