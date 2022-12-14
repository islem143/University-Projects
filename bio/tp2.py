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
            gap = int(score_mat[1][2])
           
            arr[i][j] = np.amax([int(score_mat[row_index][column_index]) +
                                 arr[i-1][j-1], arr[i-1][j]+gap, arr[i][j-1]+gap])
            if (arr[i][j] < 0):
                arr[i][j] = 0
    return arr


seq11 = "ACAATCG"
seq22 = "CTCATGC"


seq1 = "ACCGAGAC"
seq2 = "ACCGTCCCT"
# score_mat = np.array([["", "-", "A", "C", "G", "T"],
#                       ["-",  0, -2, -2, -2, -2],
#                       ["A", -2,  1, -1, -1, -1],
#                       ["C", -2, -1,  1, -1, -1],
#                       ["G", -2, -1, -1, 1, -1],
#                       ["T", -2, -1, -1, -1, 1]

#                       ])
score_mat = np.array([["", "-", "A", "C", "G", "T"],
                      ["-", 0, -1, -1, -1, -1],
                      ["A", -1,  2, -1, -1, -1],
                      ["C", -1, -1,  2, -1, -1],
                      ["G", -1, -1, -1, 2, -1],
                      ["T", -1, -1, -1, -1, 2]

                      ])
arr = local_alignement(seq11, seq22, score_mat)
print(arr)


def alignement_local_resultat(seq1, seq2, arr):
    n = arr.shape[0]
    m = arr.shape[1]
    max = np.max(arr[n-2:n, m-2:m])
    argmax = np.argmax(arr[n-2:n, m-2:m].flatten())
    n_ = argmax//2
    m_ = argmax % 2
    argmax = (n-2+n_, m-2+m_)

    i = argmax[0]
    j = argmax[1]
    h = []
    v = []

    h.append(seq2[i-1])
    v.append(seq1[j-1])
    while (i > 0 and j > 0):

        max = np.argmax([arr[i-1][j-1], arr[i][j-1], arr[i-1][j]])
        if (max == 0):

            i = i-1
            j = j-1
            v.append(seq2[i-1])
            h.append(seq1[j-1])
        elif (max == 2):
            i = i-1
            v.append(seq2[i-1])
            h.append("-")
        elif (max == 1):
            j = j-1
            v.append("-")
            h.append(seq1[j-1])

    print("H", h)
    print("V", v)


#print(alignement_local_resultat(seq11, seq22, arr))


blosum62 = np.array([

    ["", "-",  "A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L",
        "K", "M", "F", "P", "S", "T", "W", "Y", "V", "B", "Z", "X"],
    ["-", 1, -4,  -4, -4, -4, -4, -4, -4, -4, -4, -4, -
        4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4],
    ["A",  -4,  4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -
        1, -1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0],
    ["R",  -4, -1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -
        2,  2, -1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1],
    ["N", -4, -2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,
        0, -2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1],
    ["D",  -4, -2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -
        4, -1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1],
    ["C",  -4,  0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -
        1, -3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2],
    ["Q",  -4, -1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -
        2,  1,  0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1],
    ["E",  -4, -1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -
        3,  1, -2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
    ["G",  -4,  0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -
        4, -2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1],
    ["H",  -4, -2, 0, 1, -1, -3,  0,  0, -2,  8, -3, -
        3, -1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1],
    ["I",  -4, -1, -3, -3, -3, -1, -3, -3, -4, -3,  4,
        2, -3,  1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1],
    ["L",  -4, -1, -2, -3, -4, -1, -2, -3, -4, -3,  2,
        4, -2,  2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1],
    ["K",  -4, -1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -
        2,  5, -1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1],
    ["M",  -4, -1, -1, -2, -3, -1,  0, -2, -3, -2,  1,
        2, -1,  5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1],
    ["F",  -4, -2, -3, -3, -3, -2, -3, -3, -3, -1,  0,
        0, -3,  0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1],
    ["P",  -4, -1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -
        3, -1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2],
    ["S",  -4,  1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -
        2,  0, -1, -2, -1,  4,  1, -3, -2, -2,  0, 0,  0],
    ["T",  -4,  0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -
        1, -1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0],
    ["W",  -4, -3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -
        2, -3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2],
    ["Y", -4, -2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -
        1, -2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1],
    ["V",  -4,  0, -3, -3, -3, -1, -2, -2, -3, -3,  3,
        1, -2,  1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1],
    ["B",  -4, -2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -
        4,  0, -3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1],
    ["Z",  -4, -1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -
        3,  1, -1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
    ["X",  -4, 0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1]])

s1 ="ACCGACTAGACAGGT"
s2 ="TTACCGGACTAGACCAGCG"

print(local_alignement(s1, s2, blosum62))
print(alignement_local_resultat(s1, s2, local_alignement(s1, s2, blosum62)))
