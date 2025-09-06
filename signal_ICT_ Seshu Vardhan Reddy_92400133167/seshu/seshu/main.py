import numpy as np
import matplotlib.pyplot as plt
n = np.arange(20)
unit_step = np.heaviside(n, 1)
unit_impulse = np.zeros(20)
unit_impulse[10] = 1 

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.stem(n, unit_step, basefmt=" ")
plt.title('Unit Step Signal')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.subplot(2, 2, 2)
plt.stem(n, unit_impulse, basefmt=" ")
plt.title('Unit Impulse Signal')
plt.xlabel('n')
plt.ylabel('Amplitude')

# 2. Generate a sine wave of amplitude 2, frequency 5 Hz, phase 0, over 10 to 1
t = np.linspace(0, 1, 1000) 
sine_wave = 2 * np.sin(2 * np.pi * 5 * t) 
plt.subplot(2, 2, 3)
plt.plot(t, sine_wave)
plt.title('Sine Wave: A=2, f=5Hz')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 3. Perform time shifting on the sine wave by +5 units and plot both original and shifted signals
shift_amount = 5
shifted_t = t + (shift_amount / 1000)  # Adjust time axis for shifting
shifted_sine_wave = np.interp(shifted_t, t, sine_wave, left=0, right=0)  # Interpolate to align
plt.subplot(2, 2, 4)
plt.plot(t, sine_wave, label='Original')
plt.plot(shifted_t, shifted_sine_wave, label='Shifted by +5', linestyle='--')
plt.title('Original and Time-Shifted Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()

# 4. Perform addition of the unit step and ramp signal and plot the result
ramp_signal = np.arange(20)  # Ramp signal
unit_step_plus_ramp = unit_step + ramp_signal
plt.figure(figsize=(8, 6))
plt.stem(n, unit_step_plus_ramp, basefmt=" ")
plt.title('Unit Step Signal + Ramp Signal')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.show()

# 5. Multiply a sine and cosine wave of same frequency and plot the result
cosine_wave = np.cos(2 * np.pi * 5 * t) 
product_wave = sine_wave * cosine_wave  

plt.figure(figsize=(8, 6))
plt.plot(t, product_wave)
plt.title('Product of Sine and Cosine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()