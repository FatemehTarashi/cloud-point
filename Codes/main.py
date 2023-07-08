import configparser
import laspy
import numpy as np
import pyvista as pv
from sklearn.cluster import DBSCAN
from collections import Counter
from scipy.spatial import ConvexHull


from readAndPlot import plot_las_file, plot_npy_file
from statistical_Outlier_Removal_filter import sor
from groundDetection import threshold_height, ground_detection, non_ground_detection
from DBSCAN import find_big_part
from shadow import combined_with_shadow

# CONFIG
config = configparser.ConfigParser()
config.read('cp.cfg')
PATH = config.get('DATA','DATA_PATH')  # Path to the data file
NAME =config.get('DATA','DATA_NAME') # Name of the data file

# first part 
#points =plot_las_file(PATH, NAME)
#las = laspy.read(PATH) # Read las file
#points = np.vstack((las.x, las.y, las.z)).transpose() # Extract coordinates from our las file

#######

#pc = pv.PolyData(points) # Create a PyVista PolyData object for plotting
#t_hight = threshold_height(pc)

#ground_points = ground_detection(t_hight+0.3, points)
#ground_cloud = pv.PolyData(ground_points)
#ground_cloud.plot(eye_dome_lighting=True)

#non_ground_points = non_ground_detection(t_hight+0.3, points)
#non_ground_cloud = pv.PolyData(non_ground_points)
#non_ground_cloud.plot(eye_dome_lighting=True)


#afterfilterpoints = sor(non_ground_points)
#clean_cloud = pv.PolyData(afterfilterpoints)
#clean_cloud.plot(eye_dome_lighting=True)

#np.save('/home/Fatemeh/Task_Fatemetarashi/Exports/afterSOR.npy', afterfilterpoints)

######
#points = plot_npy_file('/home/Fatemeh/Task_Fatemetarashi/Exports/afterSOR.npy', 'afterSOR')

#big_part = find_big_part(points)
#np.save('/home/Fatemeh/Task_Fatemetarashi/Exports/big_part.npy', big_part)

#####
#points = plot_npy_file('/home/Fatemeh/Task_Fatemetarashi/Exports/big_part.npy', 'big_part')

#combined_points = combined_with_shadow(points)

#cloud = pv.PolyData(combined_points)
#cloud.plot(eye_dome_lighting=True)

#np.save('/home/Fatemeh/Task_Fatemetarashi/Exports/combined_points.npy', combined_points)
#####

points = plot_npy_file('/home/Fatemeh/Task_Fatemetarashi/Exports/combined_points.npy', 'combined_points')

point_cloud = pv.PolyData(points)
mesh = point_cloud.reconstruct_surface()
mesh.save('mesh.stl')

mesh.plot(color='orange')



'''
#Compute the convex hull of the point cloud
hull = ConvexHull(points)

#Get the vertices of the convex hull
vertices = points[hull.vertices]

#Create a new PyVista point cloud object
cloud = pv.PolyData(vertices)

#Create a plotter object
plotter = pv.Plotter()

#Add the point cloud object to the plotter
plotter.add_points(cloud, color='red')

#Show the plot
plotter.show()
'''









#######
#loaded_clean_points = np.load('/home/Fatemeh/Task_Fatemetarashi/Exports/clean_cloud.npy')
#clean_cloud = pv.PolyData(loaded_clean_points)
#clean_cloud.plot(eye_dome_lighting=True)

#pc = pv.PolyData(loaded_clean_points) 
#t_hight = threshold_height(pc)

#non_ground_points = non_ground_detection(t_hight, loaded_clean_points)
#non_ground_cloud = pv.PolyData(non_ground_points)
#non_ground_cloud.plot(eye_dome_lighting=True)

#np.save('/home/Fatemeh/Task_Fatemetarashi/Exports/clean_cloud2.npy', non_ground_points)

#######
#loaded_clean_points = np.load('/home/Fatemeh/Task_Fatemetarashi/Exports/clean_cloud2.npy')
#clean_cloud = pv.PolyData(loaded_clean_points)
#clean_cloud.plot(eye_dome_lighting=True)

#points = loaded_clean_points



    

