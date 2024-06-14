# Import external libraries
import argparse
# Import student libraries
from data_io import *
from preprocessing import *
from segmentation import *
from registration import *

#-----------------------------------------------------#
#                      Argparser                      #
#-----------------------------------------------------#
# Implement Argument Parser
parser = argparse.ArgumentParser(description="Medical Image Analyzer")
# Add arguments to the Argument Parser
parser.add_argument("-m", "--mode", action="store", dest="modus",
                    type=str, required=True,
                    help="Option which mode is used.\
                    Possible modes: [visualize, preproc_grayscale, \
                                    preproc_medianfilter,  preproc_gradientfilter, \
                                    preproc_contrast, segmentation, \
                                    registration]")
parser.add_argument("-i", "--input", action="store", dest="input",
                    type=str, required=True,
                    help="Path to a DICOM file.")
parser.add_argument("--reg", action="store", dest="registration",
                    type=str, required=False,
                    help="Path to a second DICOM file for registration.")
parser.add_argument("-o", "--output", action="store", dest="output",
                    type=str, default="output",
                    help="Path to the output file. File should be overwritten if existent.")
# Parse arguments
args = parser.parse_args()

#-----------------------------------------------------#
#                    Visualization                    #
if args.modus == "visualize":
    visualize(read_dicom(args.input)[1],args.output)
    quit()
#-----------------------------------------------------#

#-----------------------------------------------------#
#         Preprocessing: Grayscale Conversion         #
elif args.modus == "preproc_grayscale":
    ds, pixel_array = read_dicom(args.input)
    output_image(args.output,grayscale(pixel_array),ds)
    #visualize(grayscale(pixel_array), "testbild")
    quit()
#-----------------------------------------------------#

ds,pixel_array = read_dicom(args.input)
if len(pixel_array.shape) == 3: #is rgb
    pixel_array = grayscale(pixel_array)
visualize(pixel_array,"pretest")
#-----------------------------------------------------#
#             Preprocessing: Median Filter            #

if args.modus == "preproc_medianfilter":
    output_image(args.output,median_filter(pixel_array),ds)

#-----------------------------------------------------#

#-----------------------------------------------------#
#       Preprocessing: Gradient Filter (Sobel)        #
elif args.modus == "preproc_gradientfilter":
    output_image(args.output,gradient_filter(pixel_array), ds)
#-----------------------------------------------------#

#-----------------------------------------------------#
#         Preprocessing: Contrast Enhancement         #
elif args.modus == "preproc_contrast":
    output_image(args.output,contrast_enhancement(pixel_array),ds)
    visualize(contrast_enhancement(pixel_array), "test")
#-----------------------------------------------------#

#-----------------------------------------------------#
#               Segmentation: Threshold               #
elif args.modus == "segmentation":
    seq = thresholding(gradient_filter(median_filter(pixel_array)),25)
    im = segmentation_overlay(read_dicom(args.input)[1],seq)
    output_image(args.output,im,ds)
    visualize(im,"test")
#-----------------------------------------------------#

#-----------------------------------------------------#
#                  Registration: ORB                  #
else: #registration
    ds, pixel_array2 = read_dicom(args.registration)
    if len(pixel_array2.shape) == 3:  # is rgb
        pixel_array2 = grayscale(pixel_array2)
    registration(median_filter(gradient_filter(pixel_array)),median_filter(gradient_filter(pixel_array2)),args.output)

#-----------------------------------------------------#
