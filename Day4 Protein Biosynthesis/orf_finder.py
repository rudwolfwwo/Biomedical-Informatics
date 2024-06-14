#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#
from sequences import Sequence


#-----------------------------------------------------#
#             Open Reading Frame - Finder             #
#-----------------------------------------------------#
def get_orfs(genome,frame,min_n_codons):
    list = []
    s = genome.sequence
    i = 0
    if frame.startswith("R"):
        s = s[::-1]  # reverse
        s = s.replace("G", "B") #B temporary
        s = s.replace("C", "G")
        s = s.replace("B", "C")
        s = s.replace("T", "B")
        s = s.replace("A", "T")
        s = s.replace("B", "A")
    if frame.endswith("2"):
        i += 1
    elif frame.endswith("3"):
        i += 2

    while i + 2 < len(s):
        #print(s[i] + " " + s[i + 1] + " " + s[i + 2])
        if s[i] == "A" and s[i + 1] == "T" and s[i + 2] == "G": #start codons
            seq = Sequence(str(frame) + "." + str((i + 1)) + ".", genome.organism, "orf", "")
            j = i + 3
            while j + 2 < len(s): #end codons
                if s[j] == "T" and ((s[j + 1] == "G" and s[j + 2] == "A") or (s[j + 1] == "A" and (s[j + 2] == "A" or s[j + 2] == "G"))):
                    seq.id += str((j + 4))
                    seq.sequence = s[i:j+3]
                    if len(seq.sequence) >= min_n_codons * 3 + 4:
                        list.append(seq)
                    break
                j += 3
        i += 3
    return list

'''
Aufgabe f)
Es sind 4288 unterschiedliche Proteine annotiert
mit zusätzlichen Fällen im If-Statement in grader.py
elif args.test == "orf_finder":
    genome = data_io.read_fasta(args.input)[0]
    orf_list = orf_finder.get_orfs(genome, frame="F1", min_n_codons=150)
    print(len(orf_list)) #4144 (gleiche Größenordnung)
    data_io.write_fasta("output.txt", orf_list)
    
    
Aufgabe g)
Random Protein:
>F1.97276.98404|Escherichia coli str. K-12 substr. MG1655|protein
MAADLIVASPGIALAHPSLSAAADAGIEIVGDIELFCREAQAPIVAITGSNGKSTVTTLVGEMAKAAGVNVGVGGNIGLP
ALMLLDDECELYVLELSSFQLETTSSLQAVAATILNVTEDHMDRYPFGLQQYRAAKLRIYENAKVCVVNADDALTMPIRG
ADERCVSFGVNMGDYHLNHQQGETWLRVKGEKVLNVKEMKLSGQHNYTNALAALALADAAGLPRASSLKALTTFTGLPHR
FEVVLEHNGVRWINDSKATNVGSTEAALNGLHVDGTLHLLLGGDGKSADFSPLARYLNGDNVRLYCFGRDGAQLAALRPE
VAEQTETMEQAMRLLAPRVQPGDMVLLSPACASLDQFKNFEQRGNEFARLAKELG*

-->Name: UDP-N-acetylmuramoyl-L-alanine--D-glutamate ligase, partial [Escherichia coli]
-->Function: is a cytoplasmic enzyme involved in the biosynthesis of peptidoglycan which \
    catalyzes the addition of D-glutamate to the nucleotide precursor UDP-N-acetylmuramoyl-L-alanine (UMA)
'''

