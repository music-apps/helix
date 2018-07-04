import numpy as np
from numpy import mean, sqrt, square, arange
import librosa
import matplotlib.pyplot as plt
import matplotlib.style as ms
ms.use('seaborn-muted')
import librosa.display


class Project():
    """
        Project is a class designed to emulate a DAW style project
    """

    def __init__(self, tempo, bars, name):
        self.name = name
        self.tempo = tempo
        self.bars = bars
        self.sr = 44100  # sample rate in hz
        self.samples_per_beat = round(60 / self.tempo * self.sr)
        self.base_samples = round((60 / self.tempo * self.sr) * (self.bars * 4))
        self.audio_bed = np.zeros(self.base_samples)

    def length(self):
        """Returns length of project"""
        return len(self.audio_bed)

    def audio_sum(self, x, sample_num):
        """Adds 2 AudioTensors at a specified sample"""
        # print(len(self.audio_bed[sample_num:(sample_num+len(x))]))
        # print(len(x))
        sum_arr = self.audio_bed[sample_num:(sample_num + len(x))] + x
        self.audio_bed = np.concatenate((self.audio_bed[:sample_num], sum_arr, self.audio_bed[sample_num + len(x):]))

    def add_every_beat(self, x, start_sample):
        """ """
        sample_num = start_sample
        while (sample_num <= (self.base_samples - len(x))):
            self.audio_sum(x, sample_num)
            sample_num = sample_num + self.samples_per_beat

    def add_every_other_beat(self, x, start_sample):
        sample_num = start_sample + (self.samples_per_beat)
        while (sample_num <= (self.base_samples - len(x))):
            self.audio_sum(x, sample_num)
            sample_num = sample_num + (2 * self.samples_per_beat)

    def add_off_beat(self, x, start_sample):
        sample_num = start_sample + round(self.samples_per_beat / 2)
        while (sample_num <= (self.base_samples - len(x))):
            self.audio_sum(x, sample_num)
            sample_num = sample_num + (self.samples_per_beat)

    def add_by_pattern(self, x, start_sample, pattern):
        """ Adds audio by pattern to project base"""
        samples_per_bar = self.samples_per_beat * 4 * 4
        step_size = samples_per_bar / len(pattern)
        sample_num = start_sample
        hits = pattern.nonzero()
        while (sample_num <= (self.base_samples - (samples_per_bar))):
            for hit in np.ndenumerate(hits):
                self.audio_sum(x, sample_num + (hit[1] * round(step_size)))
            sample_num = sample_num + samples_per_bar

    def save_to_wav(self):
        """ Exports Project to Wav File """
        librosa.output.write_wav(self.name + '.wav', self.audio_bed, self.sr)

    def show_spectrogram(self):
        """ Displays an """
        S = librosa.feature.melspectrogram(self.audio_bed, sr=self.sr, n_mels=256, hop_length=50)
        log_S = librosa.power_to_db(S, ref=np.max)
        plt.figure(figsize=(10, 5))
        librosa.display.specshow(log_S, sr=self.sr, x_axis='time', y_axis='mel')
        plt.title('mel power spectrogram')
        plt.colorbar(format='%+2.0f dB')
        plt.tight_layout()
