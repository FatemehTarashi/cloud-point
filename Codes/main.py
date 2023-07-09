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
from volume import calculate_volume


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
#pc = pv.PolyData(points) 
#h = threshold_height(pc)
#height_difference = points[:, 2].max() - points[:, 2].min()
#n=0
#combined_points = combined_with_shadow(points,h+height_difference*n)

#cloud = pv.PolyData(combined_points)
#cloud.plot(eye_dome_lighting=True)

#np.save('/home/Fatemeh/Task_Fatemetarashi/Exports/combined_points.npy', combined_points)
#####

#points = plot_npy_file('/home/Fatemeh/Task_Fatemetarashi/Exports/combined_points.npy', 'combined_points')

#point_cloud = pv.PolyData(points)
#mesh = point_cloud.reconstruct_surface(progress_bar=True)
#mesh.save('/home/Fatemeh/Task_Fatemetarashi/Exports/mesh.stl')

######

#mesh = pv.read('/home/Fatemeh/Task_Fatemetarashi/Exports/mesh.stl')
#volume = mesh.volume
#print(volume)

#mesh.plot(eye_dome_lighting=True, zoom = 3)
#n=0.75
#volume = calculate_volume(points,1-n)

#with open('/home/Fatemeh/Task_Fatemetarashi/Exports/volume.txt', 'a') as f:
    #f.write(f"\nvolume{volume}  for {(n)*100}% height")

points = plot_npy_file('/home/Fatemeh/Task_Fatemetarashi/Exports/big_part.npy', 'big_part')

cloud = pv.PolyData(points)

# Create a plane at the specified height (ground level)
h =  threshold_height(cloud)
ground_level = 10
plane = pv.Plane(center=(cloud.center[0], cloud.center[1], h),
                 direction=(0, 0, 1),
                 i_size=cloud.length,
                 j_size=cloud.length)

# Extrude the point cloud to the ground plane
extruded_cloud = cloud.extrude_trim((0, 0, -1), plane)

# Visualize the original point cloud and the extruded surface
p = pv.Plotter(shape=(1, 2))
p.add_mesh(cloud, color='red')
p.add_text('Original Cloud Point', position='upper_edge')

p.subplot(0, 1)
p.add_mesh(plane, style='wireframe', color='black')
p.add_mesh(extruded_cloud, color='blue')
p.add_text('Extruded one', position='upper_edge')

p.link_views()
p.show()
