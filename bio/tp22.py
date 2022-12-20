import numpy as np


def local_alignement(seq1, seq2, score_mat):
    seq1 = np.insert(seq1, 0, "-")
    seq2 = np.insert(seq2, 0, "-")

    matrix = np.zeros((seq1.shape[0], seq2.shape[1]))

    for i in matrix.shape[0]:
        for j in matrix.shape[1]:
            



seq11 = "ACAATCG"
seq22 = "CTCATGC"
score_mat = np.array([
    [0, -1, -1, -1, -1],
    [-1,  2, -1, -1, -1],
    [-1, -1,  2, -1, -1],
    [-1, -1, -1, 2, -1],
    [-1, -1, -1, -1, 2]

])
print(local_alignement(seq11, seq22, score_mat))
