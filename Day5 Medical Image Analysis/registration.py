#-----------------------------------------------------#
#                   Library imports                   #
from skimage.feature import match_descriptors, ORB, plot_matches
import numpy as np
import matplotlib.pyplot as plt

#-----------------------------------------------------#


#-----------------------------------------------------#
#                     Registration                    #
def registration(im1,im2,path):
    de = ORB(n_keypoints=50)
    #pts = np.float([key_point.pt for key_point in de]).reshape(-1, 1, 2)
    de.detect_and_extract(im1)
    kp1 = de.keypoints
    d1 = de.descriptors

    de.detect_and_extract(im2)
    kp2 = de.keypoints
    d2 = de.descriptors

    matches12 = match_descriptors(d1, d2, cross_check=True)

    ax = plt.gca()
    #for i in range(0, 50): #red circles are not required
     #   ax.add_patch(plt.Circle((50,50), 0.2, color='r',fill=False))
    plt.axis('off')
    plt.gray()
    plot_matches(ax, im1, im2, kp1, kp2, matches12)
    plt.title("Image A vs. Image B")

    plt.show()
    plt.savefig(path)
#-----------------------------------------------------#
