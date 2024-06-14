#------------------------------------------------------------------------------#
""" Information:
Possible tests: [data_io, orf_finder, transcription, translation, aa_composition]
Example call: python grader.py --input genome.fasta --test orf_finder

If you want to use the grade for testing, be aware that data_io.py, orf_finder.py,
transcription.py... scripts have to be located in the same directory as the grader.
"""
#------------------------------------------------------------------------------#
#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
# Import student modules
import data_io
import orf_finder
import transcription
import translation
# Import external libraries
import argparse

#-----------------------------------------------------#
#                      Argparser                      #
#-----------------------------------------------------#
# Implement Argument Parser
parser = argparse.ArgumentParser(description="Grader for the Sequence Analysis")
# Add arguments to the Argument Parser
parser.add_argument("--input", action="store", dest="input", type=str, required=True)
parser.add_argument("--test", action="store", dest="test", type=str, required=True)
# Parse arguments
args = parser.parse_args()

#-----------------------------------------------------#
#                       Checks                        #
#-----------------------------------------------------#
# Check fasta reading/write function and sequence class
if args.test == "data_io":
    sequences_list = data_io.read_fasta(args.input)
    data_io.write_fasta("output.txt", sequences_list)

# Check open reading frame finder function
elif args.test == "orf_finder":
    genome = data_io.read_fasta(args.input)[0]
    orf_list = orf_finder.get_orfs(genome, frame="F1", min_n_codons=150)
    print(len(orf_list))
    data_io.write_fasta("output.txt", orf_list)

# Check transcription function
elif args.test == "transcription":
    orf_list = data_io.read_fasta(args.input)
    rna_list = []
    for orf in orf_list:
        rna = transcription.transcribe(orf)
        rna_list.append(rna)
    data_io.write_fasta("output.txt", rna_list)

# Check translation function
elif args.test == "translation":
    rna_list = data_io.read_fasta(args.input)
    protein_list = []
    for rna in rna_list:
        protein = translation.translate(rna)
        protein_list.append(protein)
    data_io.write_fasta("output.txt", protein_list)

# Check amino acid distrubtion function
elif args.test == "aa_histogram":
    # Access genome
    genome = data_io.read_fasta(args.input)[0]
    # Run Pipeline
    orf_list = orf_finder.get_orfs(genome, frame="F1", min_n_codons=150)
    protein_list = []
    for orf in orf_list:
        rna = transcription.transcribe(orf)
        protein = translation.translate(rna)
        protein_list.append(protein)
    # Evaluate
    #data_io.write_fasta("output.txt", protein_list)
    translation.aa_composition(protein_list)
