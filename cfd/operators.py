import numpy as np


def diff(f, dx, centered=True):
    if centered:
        # returns an array containing the centered difference
        # approximation to the spatial derivative of f:
        # df_i/dx \approx (f_{i+1}-f_{i-1})/(2*dx)
        # where dx is the grid spacing
        return (np.roll(f, -1)-np.roll(f, 1))/(2*dx)
    else:
        # returns an array containing the backward difference
        # approximation to the spatial derivative of f:
        # df_i/dx \approx (f_i-f_{i-1})/dx
        # where dx is the grid spacing
        return (f-np.roll(f, 1))/dx


def advection(u, f, dx, centered=True):
    # returns u f_x
    return u*diff(f, dx, centered)


def flux_form_advection(u, dx, centered=True):
    # returns F_x where F = 0.5*u**2
    return 0.5*diff(u*u, dx, centered)


def laplacian(u, dx):
    # returns the result of applying the discrete Laplacian to u
    result = (1/(dx**2))*(np.roll(u, -1) - 2*u + np.roll(u, 1))
    return result
