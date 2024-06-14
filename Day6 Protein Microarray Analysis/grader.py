#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# external libraries
import argparse
import os
# student libraries
from gpr_parser import read_gpr
from preprocessing import *
from statistics import *
from evaluation import *

#-----------------------------------------------------#
#                      Argparser                      #
#-----------------------------------------------------#
# Implement Argument Parser
parser = argparse.ArgumentParser(description="Proteome Analysis Software")
# Add arguments to the Argument Parser
parser.add_argument("--microarray", action="store", dest="microarray", type=str, required=True)
parser.add_argument("--samples", action="store", dest="samples", type=str, required=True)
parser.add_argument("--panel", action="store", dest="panel", type=str, required=True)
parser.add_argument("-t", "--test", action="store", dest="test", type=str, required=True)
# Parse arguments
args = parser.parse_args()

#-----------------------------------------------------#
#                Microarray GPR Loading               #
#-----------------------------------------------------#
# Obtain all gprs
gpr_list = os.listdir(args.microarray)
# Sort file list
gpr_list.sort()

def load_data(gpr_list):
    # Initialize combined data set
    dt = None
    # Iterate over each GPR
    for gpr_file in gpr_list:
        # Read GPR
        path_gpr = os.path.join(args.microarray, gpr_file)
        sample_id = gpr_file.split("_")[0]
        gpr = read_gpr(path_gpr, sample_id)
        # Merge with dt
        if dt is None : dt = gpr
        else : dt = dt.merge(gpr, on=["id", "position", "name"])
    return dt

# Check exercise a)
if args.test == "gpr_parser":
    dt = load_data(gpr_list)
    dt.to_csv("output.tsv", index=False, sep="\t")

#-----------------------------------------------------#
#           Preprocessing: Panel Filtering            #
#-----------------------------------------------------#
# Check exercise b)
if args.test == "panel_filtering":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_filtered.to_csv("output.tsv", index=False, sep="\t")

#-----------------------------------------------------#
#      Preprocessing: Control Spot Normalization      #
#-----------------------------------------------------#
# Check exercise c)
if args.test == "control_spot":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_processed = control_spot_norm(dt_filtered)
    dt_processed.to_csv("output.tsv", index=False, sep="\t")

#-----------------------------------------------------#
#   Preprocessing: Sample Split in Healthy & Cancer   #
#-----------------------------------------------------#
# Check exercise d) - healthy
if args.test == "sample_split_healthy":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_processed = control_spot_norm(dt_filtered)
    dt_healthy, dt_cancer = split_samples(dt_processed, args.samples)
    dt_healthy.to_csv("output.tsv", index=False, sep="\t")

# Check exercise d) - cancer
if args.test == "sample_split_cancer":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_processed = control_spot_norm(dt_filtered)
    dt_healthy, dt_cancer = split_samples(dt_processed, args.samples)
    dt_cancer.to_csv("output.tsv", index=False, sep="\t")

#-----------------------------------------------------#
#            Statistics: Median Difference            #
#-----------------------------------------------------#
# Check exercise e)
if args.test == "median_difference":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_processed = control_spot_norm(dt_filtered)
    dt_healthy, dt_cancer = split_samples(dt_processed, args.samples)
    dt_results = perform_mediandiff(dt_healthy, dt_cancer)
    dt_results.to_csv("output.tsv", index=False, sep="\t")

#-----------------------------------------------------#
#                  Statistics: T-Test                 #
#-----------------------------------------------------#
# Check exercise f)
if args.test == "t-test":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_processed = control_spot_norm(dt_filtered)
    dt_healthy, dt_cancer = split_samples(dt_processed, args.samples)
    dt_results = perform_ttests(dt_healthy, dt_cancer)
    dt_results.to_csv("output.tsv", index=False, sep="\t")

#-----------------------------------------------------#
#   Preprocessing: Sample Normalization via Z-Score   #
#-----------------------------------------------------#
# BONUS TASK check for exercise h)
if args.test == "z-score":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_processed = control_spot_norm(dt_filtered)
    dt_processed = sample_norm(dt_processed)
    dt_processed.to_csv("output.tsv", index=False, sep="\t")

#-----------------------------------------------------#
#               Evaluation: Clustering                #
#-----------------------------------------------------#
# BONUS TASK check for exercise i)
if args.test == "cluster":
    dt = load_data(gpr_list)
    dt_filtered = panel_filtering(dt, args.panel)
    dt_processed = control_spot_norm(dt_filtered)
    dt_healthy, dt_cancer = split_samples(dt_processed, args.samples)
    dt_results = perform_ttests(dt_healthy, dt_cancer)
    dt_cluster = clustering(dt_results, dt_healthy, dt_cancer)
    dt_cluster.to_csv("output.tsv", index=False, sep="\t")