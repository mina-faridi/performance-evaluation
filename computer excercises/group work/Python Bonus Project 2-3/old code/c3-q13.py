from scipy.integrate import quad
import numpy as np

def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2*np.pi)
    return(constant * np.exp((-x**2) / 2.0))


Fahrenheit = 59
mean = 10
e = 10
Celsius = (Fahrenheit - 32) * 5.0/9.0
z_upper = (Celsius - e)/mean
temperature, _ = quad(normalProbabilityDensity, np.NINF, z_upper)
print('Probability: ', temperature)