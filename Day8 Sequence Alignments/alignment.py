#-----------------------------------------------------#
#                   Library imports                   #
import numpy as np
#-----------------------------------------------------#

GAP_SCORE = -2
#-----------------------------------------------------#
#                   Needleman–Wunsch                  #

def score(A,B,m):
    if m is None:
        if A == B:
            return 1
        return -1
    return m[A][B]

def create_DP_matrix(seqA,seqB,m):
    d = GAP_SCORE
    matrix = np.zeros((len(seqA) + 1,len(seqB) + 1))
    for i in range(0,len(seqA) + 1):
        matrix[i][0] = d * i
    for j in range(0,len(seqB) + 1):
        matrix[0][j] = d * j
    for i in range(1,len(seqA) + 1):
        for j in range(1,len(seqB) + 1):
            match = matrix[i - 1][j - 1] + score(seqA[i - 1],seqB[j - 1],m)
            delete = matrix[i - 1][j] + d
            insert = matrix[i][j - 1] + d
            #print(type(insert)) # <class 'numpy.float64'> -> np.max() instead of max()
            matrix[i][j] = max(int(match),int(insert),int(delete))

    #print(matrix)
    return matrix

def backtrace(seqA,seqB,matrix,m):
    d = GAP_SCORE
    AlignmentA = ""
    AlignmentB = ""
    i = len(seqA)
    j = len(seqB)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + score(seqA[i - 1],seqB[j - 1],m): #match mismatch
            AlignmentA = seqA[i - 1] + AlignmentA
            AlignmentB = seqB[j - 1] + AlignmentB
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + d: #deletion
            AlignmentA = seqA[i - 1] + AlignmentA
            AlignmentB = '-' + AlignmentB
            i -= 1
        else: #insertion
            AlignmentA = '-' + AlignmentA
            AlignmentB = seqB[j - 1] + AlignmentB
            j -= 1
    return AlignmentA,AlignmentB

#-----------------------------------------------------#

