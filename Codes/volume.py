import numpy as np
from scipy.spatial import ConvexHull
import pyvista as pv

def calculate_volume(points):
    hull = ConvexHull(points)
    return hull.volume



