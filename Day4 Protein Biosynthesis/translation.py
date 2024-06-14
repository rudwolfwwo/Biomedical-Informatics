#-----------------------------------------------------#
#                   Library imports                   #
import matplotlib.pyplot as plt

#-----------------------------------------------------#

#-----------------------------------------------------#
#              Standard Translation Table             #
#-----------------------------------------------------#
code_sun = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
            'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
            'UAU':'Y', 'UAC':'Y', 'UAA':'*', 'UAG':'*',
            'UGU':'C', 'UGC':'C', 'UGA':'*', 'UGG':'W',
            'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
            'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
            'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
            'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
            'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
            'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
            'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
            'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
            'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
            'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
            'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
            'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}

#-----------------------------------------------------#
#                     Translation                     #
#-----------------------------------------------------#
def translate(rna):
    i = 0
    protein = ""
    while i < len(rna.sequence):
        protein += code_sun[rna.sequence[i] + rna.sequence[i + 1] + rna.sequence[i + 2]]
        i += 3
    rna.sequence = protein
    rna.type = "protein"
    return rna

#-----------------------------------------------------#
#                Amino Acid Composition               #
#-----------------------------------------------------#
def aa_composition(protein_list):
    plt.title("Amino Acid Composition in Escherichia coli")
    plt.xlabel("Amino Acid")
    plt.ylabel("Percentage")
    dic = {}
    len = 0
    for protein in protein_list:
        for letter in protein.sequence:
            len += 1
            if letter not in dic:
                if letter != '*':
                    dic[letter] = 1
            else:
                dic[letter] += 1
    plt.bar(dic.keys(), [(i * 100)/len for i in dic.values()]) #scaling down
    plt.savefig("Escherichia coli.png")
    plt.show()
