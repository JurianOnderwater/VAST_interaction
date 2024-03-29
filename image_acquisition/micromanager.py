from pycromanager import Core, Studio, Acquisition, multi_d_acquisition_events
# from ndtiff import NDTiffDataset
import matplotlib.pyplot as plt
from time import sleep
from image_acquisition.helper import rgba_to_rgb
# from file_sharing.scan_folder import Scan
# np.set_printoptions(threshold=sys.maxsize)

# bridge = Bridge()
# mmc = Core()
# mmStudio = Studio()

class Acquire():
    """
    Some description
    """

    def __init__(self, path, name: str='pycromanager_test') -> None:
        # Initialise Micromanager
        self.mmc = Core()
        self.mmStudio = Studio()
        
        # Dataset parameters
        self.path = path
        self.name = name
        # self.dataset = NDTiffDataset(dataset_path=path, remote_storage_monitor=None)

        # time series parameters
        self.exposure_time = self.mmc.get_exposure()  # in milliseconds
        self.framerate = 2 # Needs to be adapted to the turning rate of the VAST

        self.ANGLE_INCREMENT = 4 # Needs to be adapted to turning rate of the VAST
        self.NUM_IMAGES = 360/self.ANGLE_INCREMENT
        self.FILTER_COUNT = 1

        # setup cameras
        self.mmc.set_exposure(self.exposure_time)
        # mmc.set_property("BaumerOptronic", "Framerate", framerate)
        # self.auto_shutter = mmc.get_property('Core', 'AutoShutter')
        # self.light_state = mmc.get_property('Transmitted Light-State')

        self.mmc.set_property('Core', 'AutoShutter', 1)
        self.mmc.set_property('Transmitted Light', 'State', 1)
        self.property_dict = {'light level': ['Core', 'Shutter', 'Level'],
                              'light state': ['Core', 'Shutter', 'State'],
                              'zoom level' : ['ObjectiveTurret', 'State']}
        self.turret_dict   = {'10x':0,
                              '20x':1,
                              '2x':2,
                              '63x':3,
                              '4x':4} 

        # self.progress = 0
        pass

    def set_brightness(self, val: int):
        """
        Sets the brightness level to 0-255.
        
        --------
        ### Arguments:
        - `val`(int): 0-255
        """
        # self.mmc.set_property('Transmitted Light', 'State', 1)
        self.mmc.set_property('Transmitted Light', 'Level', val)
    
    def set_zoom(self, mag: str):
        """
        Sets the zoom level to one of the available options.
        
        --------
        ### Arguments:
        - `Zoom level`(str): 10x, 20x, 2x, 63x, 4x
        """
        self.mmc.set_property('ObjectiveTurret', 'State', self.turret_dict[mag])


    '''These functions are used when saving ndtiff files, not when saving individual images'''
    # def set_optical_property(self, property: str, value: int) -> None:
    #     """
    #     Sets a value of one of the optical variables.
        
    #     --------
    #     Arguments:
    #     - `property (str)` - name of the property to be set
    #         - `light state`: 0-1 (on/off)
    #         - `light level`: 0-255
    #         - `Zoom level`: 10x, 20x, 2x, 63x, 4x

    #     """
    #     # device = self.mmc.get_property(self.property_dict[property][0], self.property_dict[property][1])
    #     try:
    #         mmc.set_property(device, self.property_dict[property][2], value)
    #     except:
    #         mmc.set_property(self.property_dict[property][0], self.property_dict[property][1], self.turret_dict[value])
    #     pass


    # def acquirer(self) -> None:
    #     """
    #     Some description
    #     """
        
    #     events = multi_d_acquisition_events(num_time_points=self.NUM_IMAGES, time_interval_s=0.5)
    #     with Acquisition(directory=self.path, name=self.name, image_process_fn=helper.image_process_fn) as acq:
    #         acq.acquire(events)
    
    def snap_image(self, num: int, path: str):
        '''
        Snaps a single image and saves it as a pyplot
        --------
        ### Arguments:
        Arguments are provided automatically when using in conjunction with the `acquire()` funtion
        - `num (int)` - Index for saving puposes.
        - `path` (str) - Filepath, also for saving purposes.
        '''
        self.mmc.snap_image()
        im_name = path+ r'\vast_im_' + str(num) + '.png'
        tagged_image = self.mmc.get_tagged_image()

        pixels = tagged_image.pix.reshape(tagged_image.tags['Height'], tagged_image.tags['Width'], 4) #image consists of RGBA channels
        pixels = rgba_to_rgb(pixels)
        
        plt.imsave(fname=im_name, arr=pixels)

    def capture_series(self, num_time_points: int, time_interval: int, path: str=r"\test"):
        '''
        Runs `snap_image()` in a loop on an interval.
        --------
        ### Arguments:
        Arguments are provided automatically when using in conjunction with the `acquire()` funtion
        - `num_time_points (int)` - total amount of pictures taken.
        - `time_interval` (int) - waiting time between two pictures.
        - `path` (str) - passes path to `snap_image()`
        '''
        for i in range(num_time_points):
            self.snap_image(i, path)
            # self.progress = i
            sleep(time_interval)
            