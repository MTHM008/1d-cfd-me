import numpy as np
from cfd.operators import advection
from cfd.initial_conditions import gaussian


def test_advect_gaussian():  # INITAL CONDITION FILE - GAUSSION FUNCTION
    nx = 31  # number of grid points
    lx = 2  # length of domains
    dx = lx / (nx - 1)  # grid spacing
    x = np.linspace(0, lx, nx)  # x values

    nt = 10  # number of timesteps
    dt = 0.05  # timestep
    c = 1  # advection speed

    u = gaussian(x, 1, lx/2, 0.2)  # Gaussian initial condition

    # time loop
    for n in range(nt + 1):
        un = u.copy()
        u = un - dt * advection(c, un, dx)

    assert (np.linalg.norm(u-un) < u)
