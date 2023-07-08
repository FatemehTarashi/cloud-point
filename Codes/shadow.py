import laspy
import numpy as np
import pyvista as pv

from groundDetection import threshold_height

def combined_with_shadow(points):
    """
    Combine the original points and the projection points  

    Args:
        points: numpy.ndarray of cloud points

    Returns:
        numpy.ndarray: clean points
    """
    pc = pv.PolyData(points) # Create a PyVista PolyData object for plotting

    # Set the height for the projection
    projection_height = threshold_height(pc)  # adjust this to your needs

    # Create a copy of the points
    projection_points = points.copy()

    # Set the z-coordinate to the projection height
    projection_points[:, 2] = projection_height

    # Combine the original points and the projection points
    combined_points = np.vstack((points, projection_points))
    
    return combined_points
