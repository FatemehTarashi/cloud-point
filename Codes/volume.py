import numpy as np
from scipy.spatial import ConvexHull
import pyvista as pv
from groundDetection import threshold_height
from shadow import combined_with_shadow

def calculate_volume(points):
    """
    calculate  cloud points volume base on ground

    Args:
        points: numpy.ndarray of cloud points

    Returns:
        number: volume
    """
    hull = ConvexHull(points)
    return hull.volume

def calculate_volume(points,height_precentage):
    """
    calculate  cloud points volume base on height

    Args:
        points: numpy.ndarray of cloud points

    Returns:
        number: volume
    """
    pc = pv.PolyData(points) 
    
    #find ground hight
    h = threshold_height(pc) 
    height_difference = points[:, 2].max() - points[:, 2].min()
    combined_points = combined_with_shadow(points,h+height_difference*height_precentage)
    hull = ConvexHull(combined_points)
    return hull.volume
