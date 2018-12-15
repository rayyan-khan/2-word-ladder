import time
import math
import sys

start = time.clock()
file = open("words.txt", "r")
numNeighbors = 0
wordList = []

for line in file:
    wordList.append(line.strip())

def countWords(file):
    numWords = 0
    for line in file:
        numWords = numWords + 1
    return("Number of words: ", numWords)

def isNeighbor(word1, word2):
    matches = 0
    for n in range(0, len(word1)):
        if word1[n] == word2[n]:
            matches = matches+1
    if matches == len(word1)-1:
        return True
    else:
        return False

def toGraph(list):
    dict = {}
    for k in list:
        dict[k] = []
    for n in list:
        for m in range(len(list)):
            if isNeighbor(n,list[m]):
                dict[n].append(list[m])

    return dict

def numPairs(dict):
    total = 0
    for k in dict:
        total = total + len(dict[k])
    return total/2

def mostNeighbors(dict):
    mostNbrs = 0
    nbr = ''
    for k in dict:
        curr = len(dict[k])
        if curr > mostNbrs:
            nbr = k
            mostNbrs = curr
    return nbr

def hasNumNbrs(num, dict):
    ct = 0
    for k in dict:
        if len(dict[k])==num:
            ct = ct+1
    return ct

def numLonePairs(dict):
    ct = 0
    for k in dict:
        if len(dict[k]) == 1:
            if len(dict[dict[k][0]]) == 1:
                ct = ct + 1
    return ct/2

def findDegrees(dict):
    degLst = []
    for k in dict:
        if len(dict[k]) not in degLst:
            degLst.append(len(dict[k]))
    return degLst

def distictComponents(dict):
    sizes = set()
    for k in dict:
        seen = {k}
        parseMe = [k]
        while parseMe:
            word = parseMe.pop(0)
            for n in dict[word]:
                if n not in seen:
                    parseMe.append(n)
                    seen.add(n)
        compSize = len(seen)
        if compSize not in sizes:
            sizes.add(compSize)
    return sizes

def k3(dict):
    k3 = 0
    for k in dict:
        seen = {k}
        parseMe = [k]
        while parseMe:
            word = parseMe.pop(0)
            for n in dict[word]:
                if n not in seen:
                    parseMe.append(n)
                    seen.add(n)
            compSize = len(seen)
            if compSize == 3:
                k3 = k3+1
    return k3

def widestPair(dict):
    startWord = ''
    endWord = ''
    for k in dict:
        seen = {k}
        parseMe = [k]
        while parseMe:
            word = parseMe.pop(0)
            for n in dict[word]:
                if n not in seen:
                    parseMe.append(n)
                    seen.add(n)
            compSize = len(seen)
            if compSize == 1625:
                startWord = k
                endWord = word
    return("Start: ", startWord, " End: ", endWord)


gr = toGraph(wordList)

#part 1: count words
print(countWords(file))

#Part 2: Count pairs
print("Neighbor pairs: ", int(numPairs(gr)))

#Part 3: Print time
print("Time to do #2: ", round(time.clock()-start, 4), " seconds")

#Part 4: List neighbors of given word
#if len(sys.argv) == 2:
#    print("Word: ", sys.argv[1], " Neighbors: ", gr[sys.argv[1]] )

#Part 5: print the word with the greatest number of neighbors
print("Word with the most neighbors: ", mostNeighbors(gr))

#Part 6: print out the number of words with no neighbors
print("There are ", hasNumNbrs(0, gr), " words with 0 neighbors.")

#part 7: print out the pairs of words that only have each other as neighbors
print(numLonePairs(gr))

#part 8: print out the number of distinct degrees, and a list of the distinct degrees
lst = findDegrees(gr)
print("Number of distinct degrees: ", len(lst), '\n', "Distinct degrees: ", lst)

#part 9: print number of distict component sizes
print("Component sizes: ", len(distictComponents(gr)))

#part 10: print number of 3-cliques
print("K3s: ", k3(gr))

#bonus
print(widestPair(gr))