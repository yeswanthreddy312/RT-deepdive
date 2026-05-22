"""
Data models for the ray tracing engine.

Material: complex permittivity, refractive index, attenuation.
Ray:      origin, direction, signal tracking, path history.
"""

import numpy as np


class Material:
    """
    Electromagnetic material defined by complex relative permittivity.

    ε̃r = εr' + j·εr''
    ñ  = sqrt(ε̃r · μr)          (complex refractive index)
    α  = 4π·κ / λ0              (attenuation coefficient, Np/m)
    """
    pass


class Ray:
    """
    Mathematical ray proxy for a Poynting-vector energy path.

    origin        : np.ndarray (3,) — 3D start point
    direction     : np.ndarray (3,) — unit vector
    frequency_hz  : float           — carrier frequency
    power_dbm     : float           — signal power
    path_history  : list[np.ndarray]— visited waypoints
    bounces       : int             — interaction count
    """
    pass
