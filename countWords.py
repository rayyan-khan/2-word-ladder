file = open("words.txt", "r+")
numWords = 0
for line in file:
    if line != "\n":
        numWords = numWords+1
print("Number of words: ", numWords)