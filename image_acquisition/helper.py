import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, PngImagePlugin

def rgba2rgb(rgba: np.array) -> np.array:
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



def image_process_fn(image: np.array, metadata: dict):
    h, w, ch = 720, 1280, 4

    image = image.reshape[h,w,ch]
    image = rgba2rgb(image)
    fig = plt.plot(image)
    fig.savefig('name.png') # Take name out of metadata

    im = Image.open('name.png')
    meta = PngImagePlugin.PngInfo()

    for x in metadata:
        meta.add_text(x, metadata[x])
    im.save('name', "png", pnginfo=meta)

    return image, metadata


