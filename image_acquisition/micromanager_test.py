from pycromanager import Acquisition, multi_d_acquisition_events, Core, Studio
from ndtiff import NDTiffDataset

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


#------------------------------------------------------------------
# setup cameras
mmc.set_exposure(exposure_time)
# mmc.set_property("BaumerOptronic", "Framerate", framerate)
auto_shutter = mmc.get_property('Core', 'AutoShutter')
shutter      = mmc.get_property('Core', 'Shutter')
turret       = mmc.get_property('ObjectiveTurret', 'State')
# light_state  = mmc.get_property('Transmitted Light', 'State')
# light_level  = mmc.set_property('Transmitted Light', 'Level')


mmc.set_property('Core', 'AutoShutter', 1)
mmc.set_property(shutter, 'State', 1)
mmc.set_property(shutter, 'Level', 100)
mmc.set_property('ObjectiveTurret', 'State', 4)

# mmc.snap_image()
# tagged_image = mmc.get_tagged_image()
# #If using micro-manager multi-camera adapter, use core.getTaggedImage(i), where i is
# #the camera index

# #pixels by default come out as a 1D array. We can reshape them into an image
# print(tagged_image.pix)
# # file = open("sample.txt", "w+")

# # Saving the array in a text file
# # content = str(tagged_image.pix)
# # file.write(content)
# # file.close()

# pixels = tagged_image.pix.reshape(tagged_image.tags['Height'], tagged_image.tags['Width'], 4)
#plot it
# print(pixels3d)
# plt.imshow(pixels, cmap='gray')
# plt.show()



events = multi_d_acquisition_events(num_time_points=NUM_IMAGES, time_interval_s=0)
# angle_vast = range(NUM_IMAGES)
# for i in range(FILTER_COUNT):
#     for j in angle_vast:
#         events.append({"angle": j * NUM_IMAGES, " # in sequence": j})
    

#------------------------------------------------------------------

# with Acquisition(directory=path, name=name) as acq:
#     acq.acquire(events)



#------------------------------------------------------------------


mmc._close()