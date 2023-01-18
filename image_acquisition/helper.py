import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, PngImagePlugin

def rgba_to_rgb(rgba):
    '''
    Takes a numpy array and reshapes it into a width*height*channel shape.\n
    If an alpha channel is present it is removed.
    --------
    ### Arguments:
    - `rgba (np.array)` - pixel array.
    --------
    #### Returns:
    - rgb array in the correct shape to plot it using pyplot.
    '''
    row, col, ch = rgba.shape

    if ch == 3:
        return rgba

    assert ch == 4, 'Check if image has 4 channels.'

    rgb = np.zeros((row, col, 3), dtype='float32')
    r, g, b= rgba[:,:,0], rgba[:,:,1], rgba[:,:,2]

    rgb[:,:,0] = r
    rgb[:,:,1] = g
    rgb[:,:,2] = b

    return np.asarray(rgb, dtype='uint8')


def image_process_fn(image, metadata: dict):
    '''
    Saves images seperately instead of as a single large NDTIFF file.\n
    metadata is encoded in the png file instead of as a seperate `dict`.\n
    --------
    ### Arguments:
    Arguments are provided automatically when using in conjunction with the `acquire()` funtion
    - `image (np.array)` - pixel array.
    - `metadata` (dict) - metadata dictionary
    --------
    ### Returns:
    Input is not altered when passing through this function and are returned unchanged.
    - `original_image (np.array)` - The unchanged array of pixels.
    - `metadata` - The unchanged metadata dictionary
    '''
    h, w, ch = (720, 1280, 4) #chech image dimensions. Probably take h and w from metadata.
    original_image = image.copy()
    image = image.reshape(h,w,ch)
    image = rgba_to_rgb(image)
    fig = plt.plot(image)
    fig.savefig('actual_name_png') # Take name out of metadata

    im = Image.open('actual_name_png')
    meta = PngImagePlugin.PngInfo()

    for x in metadata:
        meta.add_text(x, metadata[x])
    im.save('name', "png", pnginfo=meta)

    return original_image, metadata

    


