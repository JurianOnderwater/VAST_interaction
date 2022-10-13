from pycromanager import Core, Studio, Acquisition, multi_d_acquisition_events
from ndtiff import NDTiffDataset
from file_sharing import scan_folder
# np.set_printoptions(threshold=sys.maxsize)

# bridge = Bridge()
mmc = Core()
mmStudio = Studio()

class Acquire():
    """
    Some description
    """

    def __init__(self, path, name: str) -> None:
        # Initialise micromanager
        self.mmc = Core()
        self.mmStudio = Studio()
        # Data set parameters
        self.path = path
        self.name = name
        self.dataset = NDTiffDataset(dataset_path=path, remote_storage_monitor=None)

        # time series parameters
        self.exposure_time = mmc.get_exposure()  # in milliseconds
        self.framerate = 2 # Needs to be adapted to the turning rate of the VAST

        self.ANGLE_INCREMENT = 4 # Needs to be adapted to turning rate of the VAST
        self.NUM_IMAGES = 360/self.ANGLE_INCREMENT
        self.FILTER_COUNT = 1

        # setup cameras
        self.mmc.set_exposure(self.exposure_time)
        # mmc.set_property("BaumerOptronic", "Framerate", framerate)
        self.auto_shutter = mmc.get_property('Core', 'AutoShutter')
        self.light_state = mmc.get_property('Transmitted Light-State')

        self.mmc.set_property('Core', 'AutoShutter', 1)
        self.mmc.set_property('Transmitted Light_State', 1)
        pass

    def acquirer(self) -> None:
        """
        Some description
        """
        events = multi_d_acquisition_events(num_time_points=self.NUM_IMAGES, time_interval_s=0.5)
        with Acquisition(directory=self.path, name=self.name) as acq:
            acq.acquire(events)
        