# Import the libraries to display matrices nicely
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the rich library for progress bar tracking and time estimation
from rich.progress import track

# Set two variables equal to two strings.
# The first string is the word you want to compare.
# The second string is the word you want to compare to.

# Import original.txt as word1
word1 = open("target.txt").read()
# Import modern.txt as word2
word2 = open("source.txt").read()

# Read each character of word1 and word2 into a list
word1 = list(word1)
word2 = list(word2)

# Compute the minimum edit distance between the two strings word1 and word2
# using the Levenshtein algorithm.


def levenshtein(str1, str2):
    """
    Calculates the Levenshtein distance between two strings.
    The Levenshtein distance is the minimum number of single-character
    edits required to transform one string into the other.
    """
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    # Create a matrix to store the distances
    matrix = []
    for i in range(len(str1) + 1):
        matrix.append([0] * (len(str2) + 1))

    # Initialize the first row and column of the matrix
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    # Track the progress of the algorithm using track
    for i in track(range(1, len(str1) + 1)):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1] + 1,
                                   matrix[i - 1][j] + 1,
                                   matrix[i][j - 1] + 1)

    num = matrix[len(str1)][len(str2)]

    # Return the whole matrix
    return matrix, num


matrix, num = levenshtein(word1, word2)
print("Levenshtein distance:",num)
print(np.matrix(matrix))
plt.imshow(matrix, cmap='tab20', interpolation='nearest')
plt.show()

# Convert the matrix into a pandas dataframe
# df = pd.DataFrame(matrix)
# print(df)