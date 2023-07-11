# cloud-point
A small program to calculate the volume of the cloud point from las file

 ## Contents
<!-- -->
- [Initial set up](#set-up)
- [Codes](#codes)
    - [configuration file](#configuration-file)
    - [python files](#python-files)
        - [readAndPlot](#readandplot)
        - [groundDetection](#grounddetection)
        - [statistical_Outlier_Removal_filter](#statistical_outlier_removal_filter)
        - [DBSCAN](#dbscan)
        - [shadow](#shadow)
        - [triangulation](#triangulation)
        - [volume](#volume)
        - [main](#main)
- [Screenshot](#screenshot)
- [Exports](#exports)
    - [numpy files](#numpy-files)
        - [afterSOR](#aftersor)
        - [big_part](#big_part)
        - [combined_points](#combined_points)
- [Information_Data](#information_data)
    - [task_rs_pc](#task_rs_pc)
    - [task_subset](#task_subset)
- [View](#view)
# set up:

We use Python environment variables to avoid configuration issues and etc.
```
$ python -m venv env
$ source env/bin/activate
```
To use the program, we navigate to the desired directory with cd!
  ```
$ cd Task_Fatemetarashi/
```
 We see four directories:
- Codes
- Screenshot
- Exports
- Information_Data 

<!-- -->
# Codes

## configuration file
Due to the fact that our ".las" file is a part of the whole and because paths are not hardcoded in the program, we have the configuration file cp.cfg

## python files
Due to the fact that we have multiple files and probably we want to perform tasks in parallel, as well as the limited power of my laptop, we have several Python files! 

### readAndPlot
This file contains 2 functions:
#### plot_las_file
Reads the initial cloud points from the .las file and displays them. like our .las file:
![cloud point](/Screenshot/0.png)
#### plot_npy_file
Reads the numpy array cloud points from the .npy file and displays them.

### groundDetection
This file contains 3 functions:
#### threshold_height
It finds the group of the points with the same height, then selects the group that has the maximum member and the lowest height and returns the height of that point.
#### ground_detection
We use the simplest method, Minimum Height Extraction. This function takes a cloud point and a height (which is basically obtained from the previous function) and recognizes the ground based on that.

For this purpose, you can use other methods such as RANSAC(Random Sample Consensus), PCA (Principal Component Analysis), or Smoothing methods like Moving Average Filtering. I think this method works better for bigger cloud point.
![ground](/Screenshot/2.png)

#### non_ground_detection
This function is the opposite of the ground_detection function

### statistical_Outlier_Removal_filter
SOR (Statistical Outlier Removal) identifies and removes outlier points based on statistical analysis of the information present in the point cloud. 

You can use Voxel Grid Filter, Radius Outlier Removal, or Conditional Outlier Removal.
![SOR filter](/Screenshot/1.png)

### DBSCAN
DBSCAN (Density-Based Spatial Clustering of Applications with Noise). DBSCAN is a density-based clustering algorithm used to detect clusters in heterogeneously distributed data as well as detect noisy points. But, here we return the largest cluster as output!
![dbscan](/Screenshot/3.png)

### shadow
This is probably not a good method, but anyway! It can be said that the shadow of the cloud sticks to it.
![shadow](/Screenshot/6.png)

### triangulation
Creates a triangulation of cloud points
![triangulation](/Screenshot/5.png)
![triangulation](/Screenshot/4.png)
### volume
It calculates the volume based on ConvexHull, based on ground or height percentage.
But, You can calculate the volume based on triangulation with mesh.volume

### main
Because this main is not supposed to be the main, no principles have been written, and mostly written for testing functions and working with cloud points. For this reason, many commands are commented!!!

<!-- -->
# Screenshot
screenshots used in the readme.

<!-- -->
# Exports 

## numpy files
Due to the speed and conditions of my system, we have a series of outputs in the form of Python files that are produced in different stages and then used.
### afterSOR
numpy array of cloud points after the SOR filter
### big_part
numpy array of cloud points after DBSCAN function( DBSCAN filter and choose the largest part
### combined_points
numpy array of cloud points after shadow function

## stl file
### mesh
mesh from triangulation

## text file
Volume calculation output

<!-- -->
# Information_Data
## task_rs_pc
The pdf file contains the purpose of this repository, i.e. the problem and its indicators
## task_subset  
The .las file contains the cloud point, a subset of a larger data cloud.

# View
If you are having trouble viewing this file, you can use [Grip](https://github.com/joeyespo/grip)  or similar tools.
