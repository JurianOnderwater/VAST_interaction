from pycromanager import Bridge, Acquisition, Core, Studio
import numpy as np
import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)

# bridge = Bridge()
mmc = Core()
mmStudio = Studio()


#------------------------------------------------------------------
# Data set parameters
path = r"\test"
name = "pycromanager test"

# rotation stack parameters
start_pos = 0
step_angle = 2  # in degrees
end_pos = 360 - step_angle
fluoresence = True # Boolean value indicating if fluoresence microscopy is being used
if fluoresence == True: filter_count = 2 
else: filter_count = 1
relative = True

# time series parameters
# duration = 2  # in seconds
exposure_time = mmc.get_exposure()  # in milliseconds
framerate = 14 # Needs to be adapted to the turning rate of the VAST


num_axis_positions = int(abs(end_pos - start_pos) / step_angle + 1)
# pos_sequence = [start_pos]
# pos_sequence += [(pos_sequence[i] + step_angle) for i in range(num_axis_positions)]
axis_idx = list(range(num_axis_positions))
# num_time_points = np.ceil(duration * framerate / num_axis_positions).astype(np.int)

#------------------------------------------------------------------
# setup cameras
mmc.set_exposure(exposure_time)
# mmc.set_roi(*ROI)
# mmc.set_property("BaumerOptronic", "Framerate", framerate)
auto_shutter = mmc.get_property('Core', 'AutoShutter')
mmc.set_property('Core', 'AutoShutter', 1)

mmc.snap_image()
tagged_image = mmc.get_tagged_image()
#If using micro-manager multi-camera adapter, use core.getTaggedImage(i), where i is
#the camera index

#pixels by default come out as a 1D array. We can reshape them into an image
print(tagged_image.pix)
file = open("sample.txt", "w+")

# Saving the array in a text file
content = str(tagged_image.pix)
file.write(content)
file.close()

pixels3d = tagged_image.pix.reshape(tagged_image.tags['Height'], tagged_image.tags['Width'], 4).transpose(2,0,1)
#plot it
# print(pixels3d)
plt.imshow(pixels3d, cmap='gray')
plt.show()



# events = []
# axis_idx_ = axis_idx.copy()
# for i in range(filter_count):
#     for j in axis_idx_:
#         events.append({"angle": pos_sequence[j], " # in sequence": j})
#     axis_idx_.reverse()

#------------------------------------------------------------------

# with Acquisition(directory=path, name=name) as acq:
#     acq.acquire(events)

#------------------------------------------------------------------
# turn off sequencing
# mmc.set_property(z_stage, "UseFastSequence", "No")
# mmc.set_property(z_stage, "UseSequence", "No")

# # move back to initial position
# mmc.set_position(z_stage, z_pos)

mmc.close()