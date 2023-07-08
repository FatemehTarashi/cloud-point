import configparser
import laspy
import numpy as np
import pyvista as pv

def plot_las_file(PATH, NAME):
    """
    Read and plot las file
    Args:
        PATH: str
        NAMe: str

    Returns:
        numpy array: cloud points
    """
    try:
        print('openning')
        las = laspy.read(PATH) # Read las file
        print('reading')
        points = np.vstack((las.x, las.y, las.z)).transpose() # Extract coordinates from our las file
        print('plotting')
        pc = pv.PolyData(points) # Create a PyVista PolyData object for plotting
        pc.plot(eye_dome_lighting=True) # Plot the PolyData
        return points #
    
    # Error handling
    except FileNotFoundError:
        print(f"File '{NAME}'not found")
    except OSError as e:
        print ("Could not read file!  ", e)
    except IOError as e:
        print("Could not open file! ", e)
        
        
def plot_npy_file(PATH, NAME):
    """
    Load and plot numpy file
    Args:
        PATH: str
        NAMe: str

    Returns:
        numpy array: cloud points
    """
    try:
        print('loading')
        loaded_points = np.load(PATH) #Load numpy file
        print('plotting')
        cloud = pv.PolyData(loaded_points) # Create a PyVista PolyData object for plotting
        cloud.plot(eye_dome_lighting=True) # Plot the PolyData
        
        return loaded_points
    
    # Error handling
    except FileNotFoundError:
        print(f"File '{NAME}'not found")
    except OSError as e:
        print ("Could not read file!  ", e)

    


            

    
