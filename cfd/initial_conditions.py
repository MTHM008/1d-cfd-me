import numpy as np
import sympy
from sympy.utilities.lambdify import lambdify


def hat(nx):
    # returns an array of length nx containing 1s for i < nx/3 and i > 2nx/3
    # and 2s for nx/3 <= i <= 2nx/3
    u = np.ones(nx)
    u[int(nx/3.): 2*int(nx/3.)] = 2.
    return u


def gaussian(x, a, b, c):
    # returns an array with ith value a exp(-(x-b)**2/(2*c**2))
    return np.asarray([a * np.exp(-(xi - b)**2 / (2 * c**2)) for xi in x])


def sawtooth(ti, xvals, nuval):
    # returns an array containing a sawtooth function
    x, nu, t = sympy.symbols('x nu t')
    phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
           sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))
    phiprime = phi.diff(x)
    u = -2 * nu * (phiprime / phi) + 4
    ufunc = lambdify((t, x, nu), u)

    return np.asarray([ufunc(ti, xi, nuval) for xi in xvals])
