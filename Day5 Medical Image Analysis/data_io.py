#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
import matplotlib.pyplot as plt
import numpy as np
import pydicom

#-----------------------------------------------------#
#                     DICOM Reader                    #
#-----------------------------------------------------#
def read_dicom(in_path):
    ds = pydicom.dcmread(in_path)
    return ds,ds.pixel_array

#-----------------------------------------------------#
#                     DICOM Writer                    #
#-----------------------------------------------------#
def output_image(out_path, image, dicom):
    # Update image in DICOM file
    if len(image.shape) == 2 or image.shape[2] == 1:
        dicom.SamplesPerPixel = 1
        dicom.PhotometricInterpretation = "MONOCHROME2"
        dicom.PlanarConfiguration = 1
    else:
        dicom.SamplesPerPixel = image.shape[2]
        dicom.PhotometricInterpretation = "RGB"
        dicom.PlanarConfiguration = 0
    dicom.PixelRepresentation = 0
    dicom.HighBit = 15
    dicom.BitsStored = 16
    dicom.BitsAllocated = 16
    if image.dtype != np.uint16:
        image = image.astype(np.uint16)
    dicom.SmallestImagePixelValue = int(image.min())
    dicom.LargestImagePixelValue = int(image.max())
    dicom.Rows = image.shape[0]
    dicom.Columns = image.shape[1]
    dicom.PixelData = image.tostring()

    # Output DICOM
    dicom.save_as(out_path)

#-----------------------------------------------------#
#                      Visualizer                     #
#-----------------------------------------------------#
def visualize(image, out_path):
    # Output png
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    else:
        plt.imshow(image)
    plt.savefig(out_path)