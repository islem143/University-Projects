import numpy as np


def local_alignement(seq1, seq2, score_mat):
    n = len(seq1)
    m = len(seq2)
    seq1 = list(seq1)

    seq2 = list(seq2)
    arr = np.zeros((m+1, n+1), dtype=np.int32)
    for i in range(1, m+1):
        for j in range(1, n+1):

            row_index = np.where(score_mat[0, :] == seq2[i-1])[0][0]
            column_index = np.where(score_mat[:, 0] == seq1[j-1])[0][0]

            gap = -2

            arr[i][j] = np.amax([int(score_mat[row_index][column_index]) +
                                 arr[i-1][j-1], arr[i-1][j]+gap, arr[i][j-1]+gap])
            if (arr[i][j] < 0):
                arr[i][j] = 0
    return arr


seq1 = "ACCGAGAC"
seq2 = "ACCGTCCCT"
score_mat = np.array([["", "-", "A", "C", "G", "T"],
                      ["-",  0, -2, -2, -2, -2],
                      ["A", -2,  1, -1, -1, -1],
                      ["C", -2, -1,  1, -1, -1],
                      ["G", -2, -1, -1, 1, -1],
                      ["T", -2, -1, -1, -1, 1]

                      ])

arr = local_alignement(seq1, seq2, score_mat)
print(arr)


def alignement_local_resultat(arr):
    n = arr.shape[0]
    m = arr.shape[1]
    max=np.max(arr[n-2:n, m-2:m])
    argmax=np.argmax(arr[n-2:n, m-2:m].flatten())
    
    
    #argmax=(n-2+argmax,m-2+argmax)
    print(argmax)


print(alignement_local_resultat(arr))
