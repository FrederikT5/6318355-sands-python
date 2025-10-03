# File consisting of different functions and operations using those functions.


import numpy as np

def generate_sine(frequency=1.0, amplitude=1.0, phase=0.0, duration=1.0, sampling_rate=1000):
    
    t = np.linspace(0, duration, int(sampling_rate*duration))
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, x

def generate_step(duration=1.0, step_time=0.5, amplitude=1.0, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate*duration))
    x = np.where(t >= step_time, amplitude, 0.0)
    return t, x


def generate_impulse(duration=1.0, impulse_time=0.0, amplitude=1.0, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate*duration))
    x = np.zeros_like(t)
    # Find index closest to impulse_time
    idx = np.argmin(np.abs(t - impulse_time))
    x[idx] = amplitude
    return t, x