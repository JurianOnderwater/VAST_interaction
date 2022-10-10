import pymmcore_plus
mmc = pymmcore_plus.CMMCorePlus.instance()  # Instance micromanager core

def print_sys_info(yn: bool):
    '''Print system info to the terminal'''
    if yn:
        mmc.getVersionInfo() # gives: 'MMCore version 2.3.2'
        mmc.getAPIVersionInfo() # gives: 'Device API version 59, Module API version 10'
    else: return
    

def load_cfg():
    '''Load devices using the .cfg file from micro-manager'''
    mmc.loadSystemConfiguration("C:/Program Files/Micro-Manager-2.0/DMI6000.cfg")
    mmc.initializeAllDevices()



if __name__ == "__main__":
    # print_sys_info(False)
    load_cfg()