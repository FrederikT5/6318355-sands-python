# File consisting of different functions and operations using those functions.

import numpy as np


def generate_sine(frequency=1.0, amplitude=1.0, phase=0.0, duration=1.0, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, x


def generate_step(duration=1.0, step_time=0.5, amplitude=1.0, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
    x = np.where(t >= step_time, amplitude, 0.0)
    return t, x


def generate_impulse(duration=1.0, impulse_time=0.0, amplitude=1.0, sampling_rate=1000):
    t = np.linspace(0, duration, int(sampling_rate*duration), endpoint=False)
    x = np.zeros_like(t)
    # Find index closest to impulse_time
    idx = np.argmin(np.abs(t - impulse_time))
    x[idx] = amplitude
    return t, x


import matplotlib.pyplot as plt

# Sine
t_sine, x_sine = generate_sine(frequency=5)
plt.plot(t_sine, x_sine)
plt.title("Sine Wave")
plt.show()

# Step
t_step, x_step = generate_step(step_time=0.3)
plt.plot(t_step, x_step)
plt.title("Unit Step")
plt.show()

# Impulse
t_imp, x_imp = generate_impulse(impulse_time=0.5)
plt.stem(t_imp, x_imp, use_line_collection=True)
plt.title("Unit Impulse")
plt.show()