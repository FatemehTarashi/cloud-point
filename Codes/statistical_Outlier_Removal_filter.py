from pyntcloud import PyntCloud
import pandas as pd
import numpy as np

def sor(points):
    """
    Apply a Statistical Outlier Removal (SOR) filter on cloud points  

    Args:
        points: numpy.ndarray of cloud points

    Returns:
        numpy.ndarray: clean points
    """
    df = pd.DataFrame(points, columns=['x', 'y', 'z'])

    # Create a PyntCloud
    cloud = PyntCloud(df)

    # Apply a Statistical Outlier Removal (SOR) filter
    #A KDTree is created to make the operation faster.
    kdtree_id = cloud.add_structure("kdtree") 
    
    # k: the number of neighbors of each point and z_max: allowed height for points.
    sor_filter = cloud.get_filter("SOR", kdtree_id=kdtree_id, k=20, z_max=1)
    
    cloud.apply_filter(sor_filter)
    return cloud.xyz
