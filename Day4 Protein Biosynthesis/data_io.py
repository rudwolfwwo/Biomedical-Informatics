#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
import re

from sequences import Sequence


#-----------------------------------------------------#
#                     Fasta Reader                    #
#-----------------------------------------------------#
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
#                     Fasta Writer                    #
#-----------------------------------------------------#
def write_fasta(path,sequence_list):
    with open(path,"w") as file:
        for seq in sequence_list:
            file.write(">" + seq.id + "|" + seq.organism + "|"  + seq.type + "\n")
            for i in range(0,len(seq.sequence)):
                if i % 80 == 0 and i != 0:
                    file.write("\n")
                file.write(seq.sequence[i])
            file.write("\n")
