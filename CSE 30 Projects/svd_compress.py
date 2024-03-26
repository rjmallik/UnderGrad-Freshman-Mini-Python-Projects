import matplotlib.pyplot as plt
from numpy import linalg as la
import numpy as np
import matplotlib.image as mpimg

def compress (img, k, debug=False):
    # apply SVD to all pixels at once
    img_transposed = np.transpose(img, (2, 0, 1))
    U, s, Vt = la.svd(img_transposed)
    print(U.shape, s.shape, Vt.shape)
    Sigma = np.zeros((Z, X, Y))
    for j in range(3):
        np.fill_diagonal(Sigma[j, :, :], s[j, :])
    k = 50    
    img_approx = U @ Sigma[..., :k] @ Vt[..., :k, :] 
    img_approx = np.transpose(img_approx, (1, 2, 0))  
    img_approx = img_approx - img_approx.min()   
    img_approx = img_approx / img_approx.max()
    plt.imshow(img_approx)  
    plt.show()
    plt.imsave("octopus_new.jpg", img_approx)


if __name__ == '__main__':

    # read the image file and display the image
    img = mpimg.imread('octopus.jpg')
    plt.imshow(img)
    plt.show()
    
    # analyze the image array
    print(img.ndim)
    print(img.shape)
    print(img.dtype)
    print(img.max())
    print(img.min())

    img_approx = compress(img, 50)
    plt.imshow(img_approx)
    plt.show()
    plt.imsave("octopus_new.jpg", img_approx)

    