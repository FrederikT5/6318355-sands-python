# This python file import the various functions from signals.py, plots and saves them.

import matplotlib.pyplot as plt
from signals import (generate_sine, generate_step, generate_impulse, time_shift, time_scale, add_signals)

# Shift and Scale on a Sine Wave

t, x = generate_sine()
t_shifted, x_shifted = time_shift(t, x, shift=0.2)
t_scaled, x_scaled = time_scale(t, x, scale=2)

# Plot Shift and Scale

plt.plot(t, x, label="Original")
plt.plot(t_shifted, x_shifted, label="Shifted")
plt.plot(t_scaled, x_scaled, label="Scaled")
plt.legend()
plt.title("Original, shifted and scaled")

# Add Sine, Step and Impulse

t, sine = generate_sine(frequency=5)
_, step = generate_step(duration=1.0, step_time=0.3, amplitude=0.5)
_, impulse = generate_impulse(impulse_time=0.7, amplitude=-1)
combined = add_signals(sine, step)
combined_2 = add_signals(combined, impulse)

# Plot Add

plt.plot(t, sine, label="Sine")
plt.plot(t, step, label="Step")
plt.plot(t, impulse, label="Impulse")
plt.legend()
plt.title("Original before Combining")

plt.figure(3) == plt.plot(t, combined_2, label="Combined")
plt.legend()
plt.title("After Combining")

plt.tight_layout()
plt.savefig("signals_output.png")
plt.show()
