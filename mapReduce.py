#!/usr/bin/env python3

#Assignment: Map Reduce
#Name: Jessica Redekop
#Professor: David Pruitt
#Due Date: Tentatively Mon. Feb. 24, 2020
#Last Modified: Mon. Feb. 24, 2020


import time
import pymp
import re

#
def dictOfItems(filesToIterate, wordList, dictOfWords):

    with pymp.Parallel(2) as p:
        
        # iterate over the list of items
        for file in p.iterate(filesToIterate):
            for line in file: 
                # get a lock for this parallel region
                sumLock = p.lock
                # Remove the leading spaces and newline character 
                # Convert the characters in line to  
                # lowercase to avoid case mismatch 
                line = line.strip().lower()
                # Split the line into words 
                line = re.sub(r"[^a-zA-Z0-9]+", ' ', line)
                # for each item take that item and
                line = line.split()
                # search for words
                for item in line: #for each word in list of words
                    for word in wordList:
                        if (word == item):
                            sumLock.acquire() # lock any other thread from accessing shared dictionary
                            dictOfWords[word] += 1
                            sumLock.release() # release lock when done

    return dictOfWords

#this method prints my formatted solution
def printResults(dictOfWords):
    print("\nThe number of occurances per word are as follows:")
    print(dictOfWords)
    print("\nThe number of occurances of all words in every document is : ")
    print(sum(dictOfWords.values()), "\n")

#this main was taken from the iterateExample.py in ExampleCode/ 
#provided by David Pruitt and modified to lead files into list
def main():
    """
    main function for when running as a script
    """
    
    #opening all shakespeare files
    infile1 = open('shakespeare1.txt',"r")
    infile2 = open('shakespeare2.txt',"r")
    infile3 = open('shakespeare3.txt',"r")
    infile4 = open('shakespeare4.txt',"r")
    infile5 = open('shakespeare5.txt',"r")
    infile6 = open('shakespeare6.txt',"r")
    infile7 = open('shakespeare7.txt',"r")
    infile8 = open('shakespeare8.txt',"r")
    
    filesToIterate = [infile1, infile2, infile3, infile4,
                      infile5, infile6, infile7, infile8]
    
    wordlist = ["hate", "love", "death", "night", "sleep", "time",
                "henry", "hamlet", "you", "my", "blood", "poison", 
                "macbeth", "king", "heart", "honest"]
    
    # create a shared dict
    dictOfWords = pymp.shared.dict()
    dictOfWords = { i : 0 for i in wordlist}
    
    dictOfWords = dictOfItems(filesToIterate,wordlist, dictOfWords)
    
    printResults(dictOfWords)

if __name__ == '__main__':
    # execute only if run as a script
    main()