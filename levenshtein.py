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

cmap = plt.cm.get_cmap('tab20_r')

# Convert a pandas dataframe to a matplotlib figure with the columns being
# labeled as word2 and the rows as word1


def df_to_plt(df, match_df):
    """
    Converts a pandas dataframe to a matplotlib figure with the columns
    being labeled as word2 and the rows as word1.
    """
    fig, ax = plt.subplots()

    # Get fig width in pixels
    fig_width_px = fig.get_figwidth() * fig.dpi

    # Get cell width in pixels
    cell_width_px = fig_width_px / len(df.columns)

    ax.imshow(match_df, cmap=cmap ,interpolation='nearest')
    ax.set_xticks(np.arange(len(df.columns)))
    ax.xaxis.tick_top()

    ax.set_yticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.columns)
    ax.xaxis.set_label_position('top')
    ax.set_yticklabels(df.index)
    plt.setp(ax.get_xticklabels())
    plt.setp(ax.get_yticklabels())
    plt.xticks(fontsize = cell_width_px / 3)
    plt.yticks(fontsize = cell_width_px / 3)

    # Scale the fontsize of the annotations to go smaller as the matrix gets larger
    plt.rcParams['font.size'] = cell_width_px / 4.5
    # Draw the annotations
    for i in range(len(df.index)):
        for j in range(len(df.columns)):
            if i == len(df.index) - 1 and j == len(df.columns) - 1:
                text = ax.text(j, i, df.iloc[i, j],
                               ha="center", va="center", color="k", fontweight='bold')
            else:
                text = ax.text(j, i, df.iloc[i, j],
                               ha="center", va="center", color="k")
    plt.tight_layout()
    plt.show()
    return fig

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

    # Create another matrix to store where the characters match up which is later used for a custom cmap in matplotlib
    match_matrix = []
    for i in range(len(str1) + 1):
        match_matrix.append([0] * (len(str2) + 1))

    # Initialize the first row and column of the matrix
    for i in range(len(str1) + 1):
        matrix[i][0] = i
    for j in range(len(str2) + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix
    # Track the progress of the algorithm using track
    for i in track(range(1, len(str1) + 1)): # Iterate over the rows
        for j in range(1, len(str2) + 1): # Iterate over the columns
            if str1[i - 1] == str2[j - 1]: # If the characters match
                matrix[i][j] = matrix[i - 1][j - 1] # Set the value to the value above and to the left
                match_matrix[i][j] = 1 # Set the match matrix to 1
            else: # If the characters don't match up, set the value to the minimum of the values above, to the left, and to the left and above
                matrix[i][j] = min(matrix[i - 1][j - 1] + 1,
                                   matrix[i - 1][j] + 1,
                                   matrix[i][j - 1] + 1)
                match_matrix[i][j] = 0 # Set the match matrix to 0

    num = matrix[len(str1)][len(str2)]

    # Return the whole matrix
    return matrix, num, match_matrix


matrix, num, match_matrix = levenshtein(word1, word2)
print("Levenshtein distance:", num)
print(np.matrix(match_matrix))

# Convert the matrix into a pandas dataframe
df = pd.DataFrame(matrix)

# Convert the match_matrix into a pandas dataframe
match_df = pd.DataFrame(match_matrix)

# Insert '_' at the beginning of the list word2
word2.insert(0, '"')
# Insert '_' at the beginning of the list word1
word1.insert(0, '"')

# Add word2 as the name of the dataframe
df.columns = word2
match_df.columns = word2

# Add word1 as the names of the rows
df.index = word1
match_df.index = word1

df_to_plt(df, match_df).savefig('levenshtein.png')
