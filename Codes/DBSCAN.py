import numpy as np
from sklearn.cluster import DBSCAN
import pyvista as pv
from collections import Counter

def find_big_part(points):
    """
    Apply a DBSCAN on cloud points  

    Args:
        points: numpy.ndarray of cloud points

    Returns:
        numpy.ndarray: bigest part of points
    """
    
    #DBSCAN
    db = DBSCAN(eps=0.3, min_samples=10).fit(points)
    labels = db.labels_

    #Number of clusters in labels, ignoring noise if present.
    n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
    n_noise_ = list(labels).count(-1)

    print('Estimated number of clusters: %d' % n_clusters_)
    print('Estimated number of noise points: %d' % n_noise_)

    # Find the label of the largest cluster
    counter = Counter(labels)
    max_cluster_label = counter.most_common(1)[0][0]

    return points[labels == max_cluster_label]
