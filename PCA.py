from PIL import Image
from numpy import *

def pca(x):
    # enter: X matrix with linearize massives, one in line
    # exit: projection matrix, dispersion, average

    # get dimension numbers
    num_data,dim = X.shape

    # centration of data
    mean_X = X.mean(axis=0)
    X = X - mean_X

    if dim>num_data:
        # PCA with compact trick
        M = dot(X,X.T) # covaration matrix
        e,EV = linalg.eigh(M) # self numbers and vectors
        tmp = dot(X.T,EV).T # compact trick
        V = tmp [::-1] # shuffle to get last vectors
        S = sqrt(e) [::-1] # shuffle to upcount

        for i in range(V.shape[1]):
            V[:i] /= S
    else:
        # PCA with singular diffusion
        U,S,V = linalg.svd(X)
        V = V[:num_data] # return only first of num_data str

    # return prjection matrix, dispersion and average
    return V,S,mean_X

