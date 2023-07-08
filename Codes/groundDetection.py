import laspy
import numpy as np
import pyvista as pv

def threshold_height(point_cloud):
    """
    Calculate the height of the maximum points that have a lower height.

    Args:
        point_cloud (Point Cloud: PyVista PolyData type): The input point cloud data

    Returns:
        float: threshold height value.
    """
    # Extracting the z-coordinates
    z_coords = point_cloud.points[:, 2]

    # Get the unique heights and their counts
    unique_heights, counts = np.unique(z_coords, return_counts=True)

    # Find the maximum count
    max_count = np.max(counts)

    # Find the z with the maximum count
    max_heights = unique_heights[counts == max_count]
    
    # We find the height of the maximum points that have a lower height.
    m_z = np.max(max_heights[max_heights < np.max(z_coords)])
    return m_z


def ground_detection(height_ground, points):
    """
    Cloud points of the ground detection  

    Args:
        height_ground: The input float number of height ground 
        points: numpy.ndarray of cloud points

    Returns:
        numpy.ndarray: ground points
    """
    # Extracting the z-coordinates
    threshold_height = height_ground
    
    # Create a mask for points below the threshold
    ground_points = points[points[:, 2] <= threshold_height]
    return ground_points

def non_ground_detection(height_ground, points):
    """
    Cloud points of the ground detection  

    Args:
        height_ground: The input float number of height ground 
        points: numpy.ndarray of cloud points

    Returns:
        numpy.ndarray: non ground points
    """
    # Extracting the z-coordinates
    threshold_height = height_ground
    
    # Create a mask for points below the threshold
    non_ground_points = points[points[:, 2] > threshold_height]
    return non_ground_points



 
