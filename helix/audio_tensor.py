import numpy as np
from numpy import mean, sqrt, square, arange
import librosa
import matplotlib.pyplot as plt
import matplotlib.style as ms

ms.use('seaborn-muted')
import librosa.display


class AudioTensor():
    """Audio Tensor is a class for importing and manipulating audio files as Numpy arrays"""

    def __init__(self, file_path):
        tensor, sr = librosa.load(file_path, mono=True, sr=44100)
        self.path = file_path  # Path to audio file
        self.sr = sr  # sr = sample rate
        self.tensor = librosa.effects.trim(tensor)[0]  # trims silence

    def rms(self):
        """Returns RMS volume of audio"""
        return sqrt(mean(square(self.tensor)))

    def gain(self, volume):
        """Gain utility. Note: NOT IN DECIBELS"""
        self.tensor = self.tensor * volume

    def rev(self):
        """Reverses audio tensor"""
        self.tensor = np.flip(self.tensor, 0)

    def show_spectrogram(self):
        """Plots a Decibel Spectrogram of the Audio Tensor"""
        S = librosa.feature.melspectrogram(self.tensor, sr=self.sr, n_mels=256, hop_length=50)
        log_S = librosa.power_to_db(S, ref=np.max)
        plt.figure(figsize=(10, 5))
        librosa.display.specshow(log_S, sr=self.sr, x_axis='time', y_axis='mel')
        plt.title('mel power spectrogram')
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()

    def normalize(self, decibels):
        """Normalize audio tensor to have peak volume of -3 db"""

        # Find current peak volume of audio file
        # Find how much gain can be applied to reach desired peak
        # Apply gain
        # return normalized audio file

        return None

    def lowpass_filter(self, cutoff, slope):
        """Apply a low_pass filter to AudioTensor"""

        # fourier transform
        # apply filter
        # reverse fourier transform
        # return filters audio

        return None