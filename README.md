# Levenshtein distance

>A string metric (string similarity metric) that measure the difference between two sequences.

- The Python file: Produces a visualization of the Levenshtein distance between two strings as a matrix.
- The Jupyter Notebook: Computes the Levenshtein distances and double metaphone values for huge .csv word lists.

# The Python file

It was made to compare two strings of text for plagiarism or similarity and has a color scheme to indicate similarities between the strings.

*New color-scheme*

![levenshtein_inversions](https://user-images.githubusercontent.com/33177286/165387940-c320b8d6-095d-47a8-baa6-afe7eb5ec918.png)

*Old colorscheme*

![levenshtein](https://user-images.githubusercontent.com/33177286/165315187-7616af9b-db3d-40a4-9d27-2b182c0babab.png)

## How to use the Python file

1. Make sure that you have the necessary dependencies such as numpy, mantplotlib and rich
2. Make sure that the two .txt files are in the same directory as the python script
3. Execute the python script by typing `python3 levenshtein.py`
4. Warning: Calculation gets very inefficient the longer the texts are

### How to change the color-scheme to the old one

Search for a line in the code that says `ax.imshow(match_df, cmap=cmap ,interpolation='nearest')` and change it to `ax.imshow(df, cmap=cmap ,interpolation='nearest')`

### How to change the colors in the color-scheme

Currently only the predefined `cmap`s from matplotlib can be used. For changing the `cmap` go to the line of code that says `cmap = plt.cm.get_cmap('tab20_r')` and change the string in the parentheses to the `cmap` of your wish.

# The Jupyter Notebook

It was made to analyze huge word dictionaries from the [OPTED](https://www.mso.anu.edu.au/~ralph/OPTED/). The Jupyter Notebook calculates the Levenshtein distances and the double metaphone values for a comparison of two words from pre-processed .CSV files extracted from the OPTED archive.

## How to use the Jupyter Notebook

1. You need to have all dictionaries as a one-column CSV file
    1. Uncompressing the hqx file
    2. Converting the HTML files to CSV
    3. Getting rid of everything else, except the words
    4. Remove duplicates
    5. Sort the words alphabetically (optional)
    6. Remove words that start with the wrong character
    
2. Have all the processed .csv files in the same dictionary as the Jupyter Notebook
3. Make sure you have installed all the necessary libraries such as `rapidfuzz.distance`, `doublemetaphone` etc.
4. Run each cell and wait for the output
