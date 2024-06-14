#--------------------------------------------------------------------------------#
# The command 'mv' stands for moving/renaming a files                            #
# -> output.tsv will be renamed to ...                                           #
#--------------------------------------------------------------------------------#
# TESTCASE A: Run 'gpr_parser' test
python grader.py --test "gpr_parser" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_A.tsv

# TESTCASE B: Run 'gpr_parser_merged' test
python grader.py --test "panel_filtering" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_B.tsv

# TESTCASE C: Run 'control_spot' test
python grader.py --test "control_spot" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_C.tsv

# TESTCASE D1: Run 'sample_split_healthy' test
python grader.py --test "sample_split_healthy" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_D.healthy.tsv

# TESTCASE D2: Run 'sample_split_cancer' test
python grader.py --test "sample_split_cancer" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_D.cancer.tsv

# TESTCASE E: Run 'median_difference' test
python grader.py --test "median_difference" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_E.tsv

# TESTCASE F: Run 't-test' test
python grader.py --test "t-test" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_F.tsv

#--------------------------------------------------------------------------------#
#                                  BONUS TASKS                                   #
#--------------------------------------------------------------------------------#
# TESTCASE H: Run 'z-score' test
python grader.py --test "z-score" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_G.tsv

# TESTCASE I: Run 'z-cluster' test
python grader.py --test "cluster" \
                 --microarray ../data/data/microarrays/ \
                 --samples ../data/data/GSE95718.samples.tsv \
                 --panel ../data/data/GSE95718.panel.tsv
mv output.tsv outputs.exercise_H.tsv
