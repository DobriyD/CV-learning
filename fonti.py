from PIL import Image
from numpy import *
from pylab import *
import PCA

im = array(Image.open(imlist[0])) # open img to get size
m,n = im.shape[0:2] # get image size
imbr = len(imlist) # get count numbers

# create the matrix for saving linearise img
immatrix = array([array(Image.open(im)).flatten()
    for im in imlist], 'f')

# run PCA
V,S,immean = PCA.PCA(immatrix)

# show few img
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range (7):
    subplot(2,4,i+2)
    imshow(V[i].reshape9m,n)

show()
