#-----------------------------------------------------#
#                   Library imports                   #
import re
import pandas as pd
#-----------------------------------------------------#

#-----------------------------------------------------#
#                     Fasta Reader                    #
def read_fasta(path):
    with open(path,"r") as file:
        lines = file.readlines()
        list = []
        seq = []
        pattern = ">(.*)\|(.*)\|(.*)"
        for line in lines:
            line = line.rstrip()
            if line.startswith(">"):
                match = re.search(pattern,line)
                new_sequence = Sequence(match.group(1),match.group(2),match.group(3),"")
                if list != []:
                    list[-1].sequence = ''.join(seq)
                    seq = []
                list.append(new_sequence)
            else:
                seq.append(line)
                #list[-1].sequence += line
        list[-1].sequence = ''.join(seq) #efficency
        return list
#-----------------------------------------------------#

#-----------------------------------------------------#
#              Substitution Matrix Reader             #
def read_matrix(path):
    return pd.read_csv(path, delimiter='\s+',skiprows=6)
#-----------------------------------------------------#

class Sequence:
    def __init__(self, id, organism, type, sequence):
        self.id = id
        self.organism = organism
        self.type = type
        self.sequence = sequence