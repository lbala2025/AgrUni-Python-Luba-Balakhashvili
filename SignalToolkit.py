import os
import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy.signal import hilbert

os.makedirs("m2_audio", exist_ok=True)


def to_int16(s):
    return (np.clip(s, -1.0, 1.0) * 32767).astype(np.int16)


def to_float(x):
    return x.astype(np.float32) / 32768.0


class SignalToolkit:
    """
    პროექტი: მოდულაცია, დემოდულაცია, ხმაური, შეფასება.
    """

    def __init__(self, fs=5000, seed=None):
        self.fs = fs
        self.rng = np.random.default_rng(seed)

    def time_vector(self, duration):
        """
        TODO: დააბრუნეთ დროის ვექტორი 0-დან duration-მდე.
        1 ქულა
        """
        return np.linspace(0, duration, int(self.fs * duration), endpoint=False)

    def am_modulate(self, message, t, fc, m=0.8):
        """
        TODO: დააბრუნეთ AM მოდულირებული სიგნალი.
        ფორმულა: s(t) = (1 + m * message) * cos(2*pi*fc*t)
        1 ქულა
        """
        return (1 + m * message) * np.cos(2 * np.pi * fc * t)

    def am_demodulate(self, am_signal, m=0.8):
        """
        TODO: აღადგინეთ სიგნალი envelope detection-ით.
        ნაბიჯები: hilbert -> abs -> (envelope - 1) / m
        1 ქულა
        """
        envelope = np.abs(hilbert(am_signal))
        return (envelope - 1) / m

    def fm_modulate(self, message, t, fc, kf=50):
        """
        TODO: დააბრუნეთ FM მოდულირებული სიგნალი.
        phase = 2*pi*fc*t + 2*pi*kf*cumsum(message)/fs
        1 ქულა
        """
        phase = 2 * np.pi * fc * t + 2 * np.pi * kf * np.cumsum(message) / self.fs
        return np.cos(phase)

    def fm_demodulate(self, fm_signal, fc, kf=50):
        """
        TODO: აღადგინეთ სიგნალი მყისიერი სიხშირით.
        hilbert -> unwrap(angle) -> diff -> (freq - fc) / kf
        1 ქულა
        """
        analytic_signal = hilbert(fm_signal)
        phase = np.unwrap(np.angle(analytic_signal))
        frequency = np.diff(phase) * self.fs / (2 * np.pi)
        return (frequency - fc) / kf

    def add_noise(self, signal, snr_db):
        """
        TODO: დაამატეთ გაუსური ხმაური მითითებული SNR-ით.
        P_signal = mean(signal**2);  P_noise = P_signal / 10**(snr_db/10)
        noise = rng.normal(0, sqrt(P_noise), signal.shape)
        1 ქულა
        """
        P_signal = np.mean(signal ** 2)
        P_noise = P_signal / (10 ** (snr_db / 10))

        noise = self.rng.normal(0, np.sqrt(P_noise), signal.shape)
        return signal + noise

    def evaluate(self, original, recovered):
        """
        TODO: დააბრუნეთ MSE. მასივები შეიძლება სხვადასხვა სიგრძის იყოს — მოჭერით მოკლემდე.
        1 ქულა
        """
        n = min(len(original), len(recovered))
        return np.mean((original[:n] - recovered[:n]) ** 2)

    def load_audio(self, path):
        """
        TODO: წაიკითხეთ .wav ფაილი.
        - განაახლეთ self.fs წაკითხული სიხშირით
        - დააბრუნეთ float სიგნალი [-1, 1] დიაპაზონში (to_float)
        - თუ dtype უკვე float-ია, დააბრუნეთ როგორც არის
        1 ქულა
        """
        self.fs, data = wavfile.read(path)

        if np.issubdtype(data.dtype, np.floating):
            return data

        return to_float(data)

    def save_audio(self, path, signal):
        """
        TODO: შეინახეთ float სიგნალი .wav ფაილად self.fs სიხშირით.
        გამოიყენეთ to_int16.
        1 ქულა
        """
        wavfile.write(path, self.fs, to_int16(signal))

    def compute_spectrum(self, signal):
        """
        TODO: დააბრუნეთ (freqs, magnitude).
        - np.fft.rfft და np.fft.rfftfreq
        - მაგნიტუდა ნორმალიზებული: abs(X) / len(signal) * 2
        1 ქულა
        """
        n = len(signal)
        spectrum = np.fft.rfft(signal)
        freqs = np.fft.rfftfreq(n, d=1 / self.fs)
        magnitude = np.abs(spectrum) / n * 2
        return freqs, magnitude

    def plot_spectrum(self, signal, title="სპექტრი", xlim=None):
        """
        TODO: გამოიყენეთ self.compute_spectrum და დახაზეთ გრაფიკი.
        1 ქულა
        """
        freqs, magnitude = self.compute_spectrum(signal)

        plt.figure(figsize=(11, 4))
        plt.plot(freqs, magnitude)
        plt.xlabel("სიხშირე (Hz)")
        plt.ylabel("ამპლიტუდა")
        plt.title(title)

        if xlim is not None:
            plt.xlim(xlim)

        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()


print("კლასი განსაზღვრულია.  ახლა შეავსეთ TODO-ები.")