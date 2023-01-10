from pycromanager import Core, Studio, Acquisition, multi_d_acquisition_events
from ndtiff import NDTiffDataset
from helper import rgba_to_rgb, image_process_fn
import time
# from file_sharing.scan_folder import Scan
# np.set_printoptions(threshold=sys.maxsize)

# mmc = Core()
# mmStudio = Studio()

class Acquire():
    """
    Some description
    """

    def __init__(self, path, name: str) -> None:
        '''Initialise µManager'''
        self.mmc = Core()
        self.mmStudio = Studio()
        
        '''Dataset parameters'''
        self.path = path
        self.default_name = 'VAST_acquisition_' + str(time())
        if name != None:
            self.name = name
        else: 
            self.name = self.default_name
        self.dataset = NDTiffDataset(dataset_path=path, remote_storage_monitor=None)
         
        '''Time series parameters'''
        self.exposure_time = self.mmc.get_exposure()     # In milliseconds
        self.framerate = 2                               # Needs to be adapted to the turning rate of the VAST

        self.ANGLE_INCREMENT = 4                         # Needs to be adapted to turning rate of the VAST
        self.NUM_IMAGES = 360/self.ANGLE_INCREMENT
        self.FILTER_COUNT = 1
        self.TIME_INTERVAL = 0.5                         # Needs to be adapted to turning rate of the VAST

        '''Setup cameras'''
        self.mmc.set_exposure(self.exposure_time)
        # mmc.set_property("BaumerOptronic", "Framerate", framerate)
        self.auto_shutter = self.mmc.get_property('Core', 'AutoShutter')
        self.light_state = self.mmc.get_property('Transmitted Light-State')

        self.mmc.set_property('Core', 'AutoShutter', 1)
        self.mmc.set_property('Transmitted Light', 'State', 1)
        self.property_dict = {'light level': ['Core', 'Shutter', 'Level'],
                              'light state': ['Core', 'Shutter', 'State'],
                              'zoom level' : ['ObjectiveTurret', 'State']}
        self.turret_dict   = {'10x':0,
                              '20x':1,
                              '2x' :2,
                              '63x':3,
                              '4x' :4,} 

    def set_optical_property(self, property: str, value: int) -> None:
        """
        Sets a value of one of the optical variables.
        
        --------
        Arguments:
        - `property (str)` - name of the property to be set
            - `light state`: 0-1 (on/off)
            - `light level`: 0-255
            - `zoom level`: 10x, 20x, 2x, 63x, 4x

        """
        device = self.mmc.get_property(self.property_dict[property][0], self.property_dict[property][1])
        try:
            self.mmc.set_property(device, self.property_dict[property][2], value)
        except: # (Deal with inconsistent naming in µManager config)
            self.mmc.set_property(self.property_dict[property][0], self.property_dict[property][1], self.turret_dict[value])


    def acquirer(self) -> None:
        """
        Some description
        """
        events = multi_d_acquisition_events(num_time_points=self.NUM_IMAGES, time_interval_s=self.TIME_INTERVAL)
        with Acquisition(directory=self.path, name=self.name, image_process_fn=image_process_fn) as acq:
            acq.acquire(events)
        