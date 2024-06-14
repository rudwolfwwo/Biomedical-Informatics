#-----------------------------------------------------#
#                   Library imports                   #
import numpy as np
from numpy import median
import math


#-----------------------------------------------------#

#-----------------------------------------------------#
#                 Grayscale Conversion                #
#-----------------------------------------------------#
def grayscale(rgb_image):
    #print(rgb_image)
    #gray = 0.299 * r + 0.587 * g + 0.114 * b
    return np.dot(rgb_image[..., :3], [0.299, 0.587, 0.114]).astype(int)


#-----------------------------------------------------#
#                    Median Filter                    #
#-----------------------------------------------------#
def median_filter(image, window_size=5):
    # Prepare
    filtered_image = np.zeros(image.shape)
    steps = math.floor((window_size - 1) / 2)
    # Iterate over each pixel
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            window_list = []

            # Obtain pixel values for window
            for x in range(i - steps,i + steps):
                for y in range(j - steps,j + steps):
                    if x > 0 and y > 0 and x < image.shape[0] and y < image.shape[1]:
                        window_list.append(image[x][y])
            # Update filtered image pixel
            filtered_image[i][j] = int(math.floor(median(window_list)))

    return filtered_image

#-----------------------------------------------------#
#       Preprocessing: Gradient Filter (Sobel)        #
#-----------------------------------------------------#
def gradient_filter(image):
    # Prepare allocate
    filtered_image = np.zeros(image.shape)
    # Iterate over each pixel except borders
    for i in range(1,image.shape[0] - 1):
        for j in range(1,image.shape[1] - 1):
            # Obtain 3x3 window
            window = image[i - 1:i + 2,j - 1:j + 2]
            # Calculate g_x and g_y
            g_x = np.sum([[-1,0,1],[-2,0,2],[-1,0,1]] * window)
            g_y = np.sum([[1, 2, 1], [0, 0, 0], [-1, -2, -1]] * window)
            # Calculate and update filtered image intensity
            pixel_intensity = math.sqrt((g_x * g_x) + (g_y * g_y))
            filtered_image[i][j] = round(pixel_intensity)

    return filtered_image

#-----------------------------------------------------#
#                 Contrast Enhancement                #
#-----------------------------------------------------#
def contrast_enhancement(image):
    # Prepare
    enhanced_image = np.zeros(image.shape)
    # Iterate over each pixel
    histogram = {i:0 for i in range(0,255)} # length 256 and value 0
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            histogram[image[i][j]] += 1
    # Calculate cumulative distribution frequency
    cdf = [i for i in range(0,255)]
    cdf[0] = histogram[0]
    for i in range(1,255):
        cdf[i] = cdf[i - 1] + histogram[i]
    # Normalize cumulative distribution frequency
    for x,ele in enumerate(cdf):
        cdf[x] = (ele * 255) / cdf[-1]
    # Assign new intensity values
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            new_val = cdf[image[i, j]]
            if new_val > 255:
                new_val = 255
            enhanced_image[i, j] = new_val
    return enhanced_image