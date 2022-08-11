from pycromanager import Bridge, Acquisition
import numpy as np

bridge = Bridge()
mmc = bridge.get_core()
mmStudio = bridge.get_studio()


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
exposure_time = 3  # in milliseconds
framerate = 1 # Needs to be adapted to the turning rate of the VAST


num_axis_positions = int(abs(end_pos - start_pos) / step_angle + 1)
pos_sequence = [start_pos]
pos_sequence += [(pos_sequence[i] + step_angle) for i in range(num_axis_positions)]
axis_idx = list(range(num_axis_positions))
# num_time_points = np.ceil(duration * framerate / num_axis_positions).astype(np.int)

#------------------------------------------------------------------
# setup cameras
mmc.set_exposure(exposure_time)
# mmc.set_roi(*ROI)
mmc.set_property("Camera", "Framerate", framerate)

# setup z stage
z_stage = mmc.get_focus_device()
# z_pos, pos_sequence = upload_piezo_sequence(
#     bridge, start_end_pos, mid_pos, step_size, relative
# )
# num_axis_positions = len(pos_sequence)

# move to first position
# mmc.set_position(z_stage, pos_sequence[0])



events = []
axis_idx_ = axis_idx.copy()
for i in range(filter_count):
    for j in axis_idx_:
        events.append({"angle": pos_sequence[j], " # in sequence": j})
    axis_idx_.reverse()

#------------------------------------------------------------------

with Acquisition(directory=path, name=name) as acq:
    acq.acquire(events)

#------------------------------------------------------------------
# turn off sequencing
# mmc.set_property(z_stage, "UseFastSequence", "No")
# mmc.set_property(z_stage, "UseSequence", "No")

# # move back to initial position
# mmc.set_position(z_stage, z_pos)

bridge.close()