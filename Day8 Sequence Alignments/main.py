#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# Import student modules
import input_reader
from input_reader import *
from alignment import *
from evaluate import *
# Import external libraries
import argparse

#-----------------------------------------------------#
#                      Argparser                      #
#-----------------------------------------------------#
# Implement Argument Parser
parser = argparse.ArgumentParser(description="Sequence Alignment Framework for the BioMedProg course")
# Add arguments to the Argument Parser
parser.add_argument("--query", action="store", dest="query", type=str, required=True)
parser.add_argument("--db", action="store", dest="db", type=str, required=True)
parser.add_argument("--sortby", action="store", dest="sortby", type=str, required=False, default="alignment")
parser.add_argument("--matrix", action="store", dest="matrix", type=str, required=False, default=None)
# Parse arguments
args = parser.parse_args()

#-----------------------------------------------------#
#            Sequence Alignment Framework             #
#-----------------------------------------------------#
# TODO: Read the database from a fasta file
db = input_reader.read_fasta(args.db)
# TODO: Read the query from a fasta file
query = input_reader.read_fasta(args.query)
# TODO: Compute alignments via Needleman-Wunsch

scores = []
i = 1
for seq in db:
    m = None
    if args.matrix is not None:
        m = read_matrix(args.matrix)
    matrix = create_DP_matrix(seq.sequence,query[0].sequence,m) #query consists of one protein
    aliscore = matrix[len(seq.sequence)][len(query[0].sequence)]
    AlignmentA,AlignmentB = backtrace(seq.sequence,query[0].sequence,matrix,m)
    identity,overlap = score_Identity(AlignmentA, AlignmentB)
    if args.sortby == "alignment":
        scores.append((seq.organism,aliscore,identity,overlap,seq.type,AlignmentA,AlignmentB))
    elif args.sortby == "identity":
        scores.append((seq.organism, aliscore, identity, overlap, seq.type, AlignmentA, AlignmentB))
        i = 2
    elif args.sortby == "overlap":
        scores.append((seq.organism, aliscore, identity, overlap, seq.type, AlignmentA, AlignmentB))
        i = 3
scores.sort(key=lambda a: a[i])
for i in range(0,len(scores)):
    print(">" + str(scores[i][0]) + "|" + str(scores[i][1]) + "|" + str(scores[i][2]) + "|" + str(scores[i][3]) + "|" + scores[i][4] + "\n",
          end='')
    print("Unknown ",end='')
    for j in range(0, len(scores[i][6])):
        if j % 80 == 0 and j != 0:
            print("\n", end='')
            print(scores[i][0] + "\t" + scores[i][5][j-80:j])
            print("Unknown ", end='')
        print(scores[i][6][j], end='')
    print("\n", end='')
    print(scores[i][0] + "\t" + scores[i][5][len(scores[i][6]) - len(scores[i][6]) % 80:len(scores[i][6])])
# TODO: Score alignments via alignment-score, identity & overlap

# TODO: Output alignments & scores to stdout in the correct pre-defined format


