import numpy as np
import matplotlib.pyplot as plt

fs = 2000
duration = 2
t = np.linspace(0, duration, int(fs * duration), endpoint=False)


f = np.array([5, 12, 30])
Amp = np.array([1.0, 0.5, 0.25])


s1 = Amp[0] * np.sin(2 * np.pi * f[0] * t)
s2 = Amp[1] * np.sin(2 * np.pi * f[1] * t)
s3 = Amp[2] * np.sin(2 * np.pi * f[2] * t)

signal = s1+s2+s3


print("Min:", np.min(signal))
print("Max:", np.max(signal))
print("Mean:", np.mean(signal))
print("RMS:", np.sqrt(np.mean(signal**2)))

plt.figure(figsize=(12, 4))
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Signal vs Time")
plt.grid(True)
plt.show()
