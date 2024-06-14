#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
import numpy as np

#-----------------------------------------------------#
#                     Thresholding                    #
#-----------------------------------------------------#
def thresholding(image, threshold_value):
    seq = np.zeros(image.shape)
    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if image[i][j] >= threshold_value:
                seq[i][j] = 1
            else:
                seq[i][j] = 0
    return seq

#-----------------------------------------------------#
#                 Segmentation Overlay                #
#-----------------------------------------------------#
def segmentation_overlay(image, seg):
    # Initialize segmentation in RGB
    seg_rgb = np.zeros((seg.shape[0], seg.shape[1], 3), dtype=int)
    # Set binary segmentation to appropriate color (blue)
    seg_rgb[np.equal(seg, 1)] = [0, 0, 255]
    # Get binary array for places where an ROI lives
    segbin = np.greater(seg, 0)
    repeated_segbin = np.stack((segbin, segbin, segbin), axis=-1)
    # Weighted sum where there's a value to overlay
    alpha = 0.3                         # alpha = overlay transparency
    image_overlayed = np.where(
        repeated_segbin,
        np.round(alpha*seg_rgb + (1-alpha)*image).astype(np.uint8),
        np.round(image).astype(np.uint8)
    )
    # Return final image with segmentation overlay
    return image_overlayed
