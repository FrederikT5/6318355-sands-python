# File consisting of different functions and operations using those functions.

# Singals

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

# Operations

def time_shift(t, x, shift=0.0):
    t_shifted = t + shift
    return t_shifted, x


def time_scale(t, x, scale=1.0):
    t_scaled = t * scale
    return t_scaled, x

def add_signals(x1, x2):
    if len(x1) != len(x2):
        raise ValueError("Signals must have the same length for addition.")
    return x1 + x2
