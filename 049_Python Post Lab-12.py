#Generate two sine wave signals with frequencies of 5 Hz and 10 Hz, both sampled at 1000 Hz for 1 second. Add the two signals together and plot the result.
import numpy as np
import matplotlib.pyplot as plt
fs = 1000
t = np.arange(0, 1, 1/fs)
sine1 = np.sin(2 * np.pi * 5 * t)
sine2 = np.sin(2 * np.pi * 10 * t)
combined = sine1 + sine2
plt.figure(figsize=(10, 6))
plt.plot(t, sine1, label='5 Hz Sine')
plt.plot(t, sine2, label='10 Hz Sine')
plt.plot(t, combined, label='Combined Signal', linewidth=2)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Sine Waves and Their Sum")
plt.legend()
plt.grid(True)
plt.show()

#Generate a 5 Hz sine wave and a 10 Hz cosine wave, both sampled at 500 Hz for 2 seconds. Multiply the two signals element-wise and plot the resulting signal.
import numpy as np
import matplotlib.pyplot as plt
fs = 500     
t = np.arange(0, 2, 1/fs)   
sine_5hz = np.sin(2 * np.pi * 5 * t)
cosine_10hz = np.cos(2 * np.pi * 10 * t)
result = sine_5hz * cosine_10hz
plt.figure(figsize=(10, 4))
plt.plot(t, result, label='5 Hz sine × 10 Hz cosine')
plt.title('Product of 5 Hz Sine and 10 Hz Cosine')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


#Generate a 5 Hz sine wave signal and shift it in time by 0.1 seconds. Plot the original and shifted signals on the same graph for comparison
import numpy as np
import matplotlib.pyplot as plt
fs = 500
t = np.arange(0, 1, 1/fs)   
sine_5hz = np.sin(2 * np.pi * 5 * t)
shifted_sine = np.sin(2 * np.pi * 5 * (t - 0.1))
plt.figure(figsize=(10, 4))
plt.plot(t, sine_5hz, label='Original 5 Hz Sine')
plt.plot(t, shifted_sine, label='Shifted by 0.1s', linestyle='--')
plt.title('5 Hz Sine Wave and Time-Shifted Version')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


#Generate a 10 Hz sine wave and scale its amplitude by a factor of 3. Plot the original and scaled signals together.
import numpy as np
import matplotlib.pyplot as plt
fs = 500   
t = np.arange(0, 1, 1/fs)
sine_10hz = np.sin(2 * np.pi * 10 * t)
scaled_sine = 3 * sine_10hz
plt.figure(figsize=(10, 4))
plt.plot(t, sine_10hz, label='Original 10 Hz Sine')
plt.plot(t, scaled_sine, label='Scaled by factor 3', linestyle='--')
plt.title('10 Hz Sine Wave (Original vs Scaled)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


#Generate a 5 Hz sine wave and reverse it in time. Plot the original and reversed signals on the same graph. 
import numpy as np
import matplotlib.pyplot as plt
fs = 500      
t = np.arange(0, 1, 1/fs)   
sine_5hz = np.sin(2 * np.pi * 5 * t)
reversed_sine = sine_5hz[::-1]
t_reversed = t                   
plt.figure(figsize=(10, 4))
plt.plot(t, sine_5hz, label='Original 5 Hz Sine')
plt.plot(t_reversed, reversed_sine, label='Time-Reversed', linestyle='--')
plt.title('5 Hz Sine Wave (Original vs Time-Reversed)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()

