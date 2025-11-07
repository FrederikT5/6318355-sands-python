# Tests verifying various signal generation functions and operations on those signals.

from signals import *
import numpy as np

def test_generate_sine():
    """
    Verifies that the generate_sine function works correctly with different inputs.
    
    Tests include:
    - Signal length verification
    - Initial value check
    - Amplitude validation
    - Zero amplitude case
    """
    t, x = generate_sine(frequency=1, amplitude=1, phase=0, duration=10, sampling_rate=1000)
    assert len(t) == 10000
    assert np.isclose(x[0], 0, atol=1e-6)

    t, x = generate_sine(frequency=1, amplitude=3, phase=0, duration=10, sampling_rate=1000)
    assert np.isclose(np.max(x), 3, atol=1e-3)

    t, x = generate_sine(frequency=1, amplitude=0, phase=0, duration=10, sampling_rate=1000)
    assert np.allclose(x, 0)

def test_generate_step():
    """
    Verifies that the generate_step function works correctly with different inputs.
    
    Tests include:
    - Signal length verification
    - Step timing and value verification
    - Amplitude validation
    - Zero amplitude case
    """
    t, x = generate_step(duration=10, step_time=5, amplitude=1, sampling_rate=1000)
    assert len(t) == 10000
    assert x[0] == 0
    assert x[5000] == 1

    t, x = generate_step(duration=10, step_time=5, amplitude=3, sampling_rate=1000)
    assert np.isclose(np.max(x), 3, atol=1e-3)

    t, x = generate_step(duration=10, step_time=5, amplitude=0, sampling_rate=1000)
    assert np.allclose(x, 0)

def test_generate_impulse():
    """
    Verifies that the generate_impulse function works correctly with different inputs.
    
    Tests include:
    - Signal length verification
    - Impulse timing and value verification
    - Amplitude validation
    - Zero amplitude case
    """
    t, x = generate_impulse(duration=10, impulse_time=5, amplitude=1, sampling_rate=1000)
    assert len(t) == 10000
    impulse_index = np.argmin(np.abs(t - 5))
    assert x[impulse_index] == 1

    t, x = generate_impulse(duration=10, impulse_time=5, amplitude=3, sampling_rate=1000)
    assert np.isclose(np.max(x), 3, atol=1e-3)

    t, x = generate_impulse(duration=10, impulse_time=5, amplitude=0, sampling_rate=1000)
    assert np.allclose(x, 0)

def test_time_shift():
    """
    Verifies that the time_shift operation works correctly with different inputs.
    
    Tests include:
    - Correct shifting of the time vector
    - Signal values remain unchanged
    """
    t = np.linspace(0, 10, 1000)
    x = np.ones_like(t)
    t_shifted, x_shifted = time_shift(t, x, shift=2)
    assert np.allclose(t_shifted, t + 2)
    assert np.allclose(x_shifted, x)

def test_time_scale():
    """
    Verifies that the time_scale operation works correctly with different inputs.
    
    Tests include:
    - Correct scaling of the time vector
    - Signal values remain unchanged
    """
    t = np.linspace(0, 10, 1000)
    x = np.ones_like(t)
    t_scaled, x_scaled = time_scale(t, x, scale=0.5)
    assert np.allclose(t_scaled, t * 0.5)
    assert np.allclose(x_scaled, x)

def test_add_signals():
    """
    Verifies that the add_signals operation works correctly with different inputs.
    
    Tests include:
    - Correct element-wise addition of two signals
    """
    x1 = np.array([1, 2, 3])
    x2 = np.array([4, 5, 6])
    result = add_signals(x1, x2)
    assert np.array_equal(result, np.array([5, 7, 9]))
