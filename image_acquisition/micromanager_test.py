from pycromanager import Acquisition, multi_d_acquisition_events, Core, Studio
from ndtiff import NDTiffDataset
from helper import rgba_to_rgb, image_process_fn
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from PIL import Image, PngImagePlugin

# bridge = Bridge()
mmc = Core()
mmStudio = Studio()


#------------------------------------------------------------------
# Data set parameters
path = r"\test"
name = "pycromanager_test"

# time series parameters
# duration = 2  # in seconds
exposure_time = mmc.get_exposure()  # in milliseconds
framerate = 14 # Needs to be adapted to the turning rate of the VAST

ANGLE_INCREMENT = 120
NUM_IMAGES = int(360/ANGLE_INCREMENT)
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

# mmc.set_property('Core', 'AutoShutter', 1)
mmc.set_property('Transmitted Light', 'Level', 150)
mmc.set_property('Transmitted Light', 'State', 1)
mmc.set_property('ObjectiveTurret', 'State', 4)

channel_group = "channel-group-name"
channels = ["BF", "FL"]
# channel_exposures_ms = [15.5, 200]

"""Test snapping a single image"""


# mmc.snap_image()
# tagged_image = mmc.get_tagged_image()

# pixels = tagged_image.pix.reshape(tagged_image.tags['Height'], tagged_image.tags['Width'], 4)
# pixels = rgba_to_rgb(pixels)
# # print(pixels)
# plt.imshow(pixels, cmap='hsv')
# plt.show()


"""Test acquiring a series of events"""

def snap_image(num: int, path: str):
    mmc.snap_image()
    im_name = path+ r'\vast_im_' + str(num)
    tagged_image = mmc.get_tagged_image()

    pixels = tagged_image.pix.reshape(tagged_image.tags['Height'], tagged_image.tags['Width'], 4)
    pixels = rgba_to_rgb(pixels)
    # fig = plt.imshow(pixels)
    # fig.savefig(im_name) # Take name out of metadata

    # im = Image.open(im_name)
    # meta = PngImagePlugin.PngInfo()
    # # meta.add_text(x, metadata[x])
    # im.save(im_name, "png", pnginfo=meta)
    # plt.imshow(pixels)
    plt.imsave(fname=im_name+'.png', arr=pixels)
    plt.show()

def capture_series(num_time_points: int, time_interval: int, path: str=r"\test"):
    for i in range(num_time_points):
        snap_image(i, path)
        sleep(time_interval)

capture_series(2,1)
        
# events = multi_d_acquisition_events(num_time_points=NUM_IMAGES, time_interval_s=VAST_CAPTURE_INTERVAL)
# events = []
# angle_vast = range(NUM_IMAGES)
# for i in range(FILTER_COUNT):
#     for j in angle_vast:
#         events.append({"angle": j * NUM_IMAGES, " # in sequence": j})
    
# events = multi_d_acquisition_events(
#                                     num_time_points=4, time_interval_s=1,
#                                     )
#------------------------------------------------------------------

# with Acquisition(directory=path, name=name) as acq:
#     acq.acquire(events)



#------------------------------------------------------------------


mmc._close()