#-----------------------------------------------------#
#                   Library imports                   #
#-----------------------------------------------------#

#-----------------------------------------------------#
#             Sequence Similarity Scoring             #
def score_Identity(aliA,aliB):
    if len(aliA) != len(aliB):
        raise Exception
    matches = 0
    for i in range(0,len(aliA)): #should have same len
        if aliA[i] == aliB[i]:
            matches += 1
    overlap = matches/len(aliA)
    identity = matches/len(aliB.replace('-',''))
    return round(identity,4),round(overlap,4)
#-----------------------------------------------------#

