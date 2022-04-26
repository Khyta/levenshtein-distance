# Levenshtein distance

>A string metric (string similarity metric) that measure the difference between two sequences.

This code also produces a visualization of the Levenshtein distance as a matrix where the bottom right number is highlighted to show the Levenshtein distance.

*New color-scheme*

![levenshtein_inversions](https://user-images.githubusercontent.com/33177286/165387940-c320b8d6-095d-47a8-baa6-afe7eb5ec918.png)

*Old colorscheme*

![levenshtein](https://user-images.githubusercontent.com/33177286/165315187-7616af9b-db3d-40a4-9d27-2b182c0babab.png)


## How to use

1. Make sure that you have the necessary dependencies such as numpy, mantplotlib and rich
2. Make sure that the two .txt files are in the same directory as the python script
3. Execute the python script by typing `python3 levenshtein.py`
4. Warning: Calculation gets very inefficient the longer the texts are

### How to change the color-scheme to the old one

Search for a line in the code that says `ax.imshow(match_df, cmap=cmap ,interpolation='nearest')` and change it to `ax.imshow(df, cmap=cmap ,interpolation='nearest')`

### How to change the colors in the color-scheme

Currently only the predefined `cmap`s from matplotlib can be used. For changing the `cmap` go to the line of code that says `cmap = plt.cm.get_cmap('tab20_r')` and change the string in the parentheses to the `cmap` of your wish.
