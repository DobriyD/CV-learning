from PIL import Image
from numpy import *
import matplotlib.pyplot as plt

def histeq(im, nbr_bins=256):
# Histogram distribution of halftone image.
    # Get histogram f image
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() # distribution func
    cdf = 255 * cdf / cdf[-1] # normize

    # using linear interpolation cdf for number of new pixels
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf


im = array(Image.open('empire.jpg').convert('L'))
im2,cdf = histeq(im)

plt.imshow(im2)
plt.savefig('output.jpg')
