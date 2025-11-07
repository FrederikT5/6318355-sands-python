# File consisting of different functions and operations using those functions.

# Signals

import numpy as np

def generate_sine(frequency=1.0, amplitude=1.0, phase=0.0, duration=1.0, sampling_rate=1000):
    """Generate a sine wave signal.

    Parameters:
        frequency (float): frequency in Hz
        amplitude (float): amplitude of the wave
        phase (float): phase in radians
        duration (float): total duration in seconds
        sampling_rate (int): number of samples per second

    Returns:
        tuple: (t, x) where t is the time vector and x is the sine wave signal.
    """
    t = np.linspace(0, duration, int(sampling_rate*duration))
    x = amplitude * np.sin(2 * np.pi * frequency * t + phase)
    return t, x


def generate_step(duration=1.0, step_time=0.5, amplitude=1.0, sampling_rate=1000):
    """Generate a step signal.

    Parameters:
        duration (float): total duration in seconds
        step_time (float): time at which the step occurs
        amplitude (float): step amplitude
        sampling_rate (int): samples per second

    Returns:
        tuple: (t, x) where t is the time vector and x is the step signal.
    """
    t = np.linspace(0, duration, int(sampling_rate*duration))
    x = np.where(t >= step_time, amplitude, 0.0)
    return t, x


def generate_impulse(duration=1.0, impulse_time=0.0, amplitude=1.0, sampling_rate=1000):
    """Generate an impulse signal.

    Parameters:
        duration (float): total duration in seconds
        impulse_time (float): time at which the impulse occurs
        amplitude (float): impulse amplitude
        sampling_rate (int): samples per second

    Returns:
        tuple: (t, x) where t is the time vector and x is the impulse signal.
    """
    t = np.linspace(0, duration, int(sampling_rate*duration))
    x = np.zeros_like(t)
    # Find index closest to impulse_time
    idx = np.argmin(np.abs(t - impulse_time))
    x[idx] = amplitude
    return t, x


def time_shift(t, x, shift=0.0):
    """Shift a signal in time.

    Parameters:
        t (np.ndarray): time vector
        x (np.ndarray): signal values
        shift (float): time shift (positive = shift right, negative = shift left)

    Returns:
        tuple: (t_shifted, x) where t_shifted is the shifted time vector.
    """
    t_shifted = t + shift
    return t_shifted, x


def time_scale(t, x, scale=1.0):
    """Scale a signal in time.

    Parameters:
        t (np.ndarray): time vector
        x (np.ndarray): signal values
        scale (float): time scaling factor ( >1 = stretch, <1 = compress)

    Returns:
        tuple: (t_scaled, x) where t_scaled is the scaled time vector.
    """
    t_scaled = t * scale
    return t_scaled, x


def add_signals(x1, x2):
    """Add two signals element-wise.

    Parameters:
        x1 (np.ndarray): first signal
        x2 (np.ndarray): second signal (must be same length as x1)

    Returns:
        np.ndarray: element-wise sum of the two input signals.
    """
    if len(x1) != len(x2):
        raise ValueError("Signals must have the same length for addition.")
    return x1 + x2
