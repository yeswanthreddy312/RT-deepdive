"""
Ray-surface intersection engine.

Surface               : polygon vertex array + Material.
ray_triangle_intersect: Möller–Trumbore algorithm (pure numpy).

Return payload: (hit: bool, t: float, point: ndarray(3,), normal: ndarray(3,))
  - t      retained for FSPL = (4πd/λ)²
  - point  absolute 3D hit coordinate
  - normal unit surface normal at hit location
"""

import numpy as np
from .core import Material, Ray


class Surface:
    """Geometric surface: sequence of 3D polygon vertices mapped to a Material."""
    pass


def ray_triangle_intersect(ray: Ray, surface: Surface) -> tuple:
    """Möller–Trumbore intersection — implementation pending."""
    raise NotImplementedError
