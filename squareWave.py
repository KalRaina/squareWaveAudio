from scipy.io.wavfile import write
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

sampleRate = 44100 # samples per second
duration = 10.0 # time
f = 440 # fundamental frequency

x = np.linspace(0,duration,int(sampleRate*duration), endpoint=False)

t = np.linspace(0, duration, int(sampleRate * duration), endpoint = False) # time axis

wave = np.zeros_like(t) # array of zeros matching size of t

N = 1000 # amount of times the loop will repeat to give 50 terms of fourier expansion for each element

# adds the fourier series expansion for square wave (odd harmonics, 50 terms) to each element 
# that represents the time intervals

for n in range(1, N+1, 2):  

    coefficient = 1 / n
    wave += coefficient * np.sin(2 * np.pi * n * f * t) # vectorised operation, does it for the entire array
    # t value not the same for every element in array so diff values achieved 

wave = wave/np.max(np.abs(wave)) # normalise to range -1 to 1 by dividing everything by largest value

# like dividing both the numerator and denominator of a fraction to simplify it, smaller number represention
# but same values (wave shape in this case)
# another example is like multiplying a vector by a scalar, diff magnitude same direction

wave = wave * 32767 # stretches it to normal amplitude for playing
wave = wave.astype(np.int16) # needed for WAV audio

write("square.wav", sampleRate, wave) # writes to wav file

plt.plot(x[:200], wave[:200].astype(float)/32767) # plots square wave 
plt.show()

sd.play(wave, sampleRate) # plays the sound through speakers
sd.wait()