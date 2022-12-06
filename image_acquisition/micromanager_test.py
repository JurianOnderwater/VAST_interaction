from pycromanager import Acquisition, multi_d_acquisition_events, Core, Studio
from ndtiff import NDTiffDataset
import matplotlib.pyplot as plt
import numpy as np

# bridge = Bridge()
mmc = Core()
mmStudio = Studio()


#------------------------------------------------------------------
# Data set parameters
path = r"\test"
name = "pycromanager_test"
# dataset = NDTiffDataset(dataset_path=path, remote_storage_monitor=None)


# time series parameters
# duration = 2  # in seconds
exposure_time = mmc.get_exposure()  # in milliseconds
framerate = 14 # Needs to be adapted to the turning rate of the VAST

ANGLE_INCREMENT = 120
NUM_IMAGES = 360/ANGLE_INCREMENT
FILTER_COUNT = 1
VAST_CAPTURE_INTERVAL = 1


#------------------------------------------------------------------
# setup cameras
mmc.set_exposure(exposure_time)
# mmc.set_property("BaumerOptronic", "Framerate", framerate)
auto_shutter = mmc.get_property('Core', 'AutoShutter')
# shutter      = mmc.get_property('Core', 'Shutter')
turret       = mmc.get_property('ObjectiveTurret', 'State')
# light_state  = mmc.get_property('Transmitted Light', 'State')
# light_level  = mmc.set_property('Transmitted Light', 'Level')

mmc.set_property('Core', 'AutoShutter', 1)
mmc.set_property('Transmitted Light', 'Level', 100)
mmc.set_property('Transmitted Light', 'State', 1)
mmc.set_property('ObjectiveTurret', 'State', 4)

channel_group = "channel-group-name"
channels = ["BF", "FL"]
# channel_exposures_ms = [15.5, 200]

"""Test snapping a single image"""

def rgba2rgb(rgba: np.array):
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4, 'RGBA image has 4 channels.'

    rgb = np.zeros( (row, col, 3), dtype='float32' )
    r, g, b= rgba[:,:,0], rgba[:,:,1], rgba[:,:,2]

    rgb[:,:,0] = r
    rgb[:,:,1] = g
    rgb[:,:,2] = b

    return np.asarray( rgb, dtype='uint8' )

mmc.snap_image()
tagged_image = mmc.get_tagged_image()

pixels = tagged_image.pix.reshape(tagged_image.tags['Height'], tagged_image.tags['Width'], 4)
pixels = rgba2rgb(pixels)
print(pixels)
plt.imshow(pixels, cmap='hsv')
plt.show()


"""Test acquiring a series of events"""
# events = multi_d_acquisition_events(num_time_points=NUM_IMAGES, time_interval_s=VAST_CAPTURE_INTERVAL)
# angle_vast = range(NUM_IMAGES)
# for i in range(FILTER_COUNT):
#     for j in angle_vast:
#         events.append({"angle": j * NUM_IMAGES, " # in sequence": j})
    

#------------------------------------------------------------------

# with Acquisition(directory=path, name=name) as acq:
#     acq.acquire(events)



#------------------------------------------------------------------


mmc._close()