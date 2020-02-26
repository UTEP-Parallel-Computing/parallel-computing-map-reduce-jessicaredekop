#!/usr/bin/env python3

#Assignment: Map Reduce
#Name: Jessica Redekop
#Professor: David Pruitt
#Due Date: Tentatively Mon. Feb. 24, 2020
#Last Modified: Mon. Feb. 24, 2020


import time
import pymp
import re

def dictOfItems(linesToIterate, wordList):
    
    # create a shared dict
    dictOfWords = pymp.shared.dict()
    #initialize dictionary with WordList
    #for i in wordList:
    #    dictOfWords[i] = 0
            
    with pymp.Parallel(1) as p:
       
        for i in wordList:
            dictOfWords[i] = 0
            
        localDictOfWords = {}
        
        #get a lock for this parallel region
        sumLock = p.lock
        # iterate over the list of items
        for line in p.iterate(linesToIterate):
            for i in wordList:
                localDictOfWords[i] = 0
            #print('help1')
            #if p.thread_num is not 1:
            #p.print("Calculating from thread {} of {}".format(p.thread_num, p.num_threads))
            #print('help2')
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
                        #sumLock.acquire() # lock any other thread from accessing shared dictionary
                        localDictOfWords[word] += 1
                        #sumLock.release() # release lock when done
            for word in wordList:
                sumLock.acquire() # lock any other thread from accessing shared dictionary
                dictOfWords[word] += localDictOfWords[word]
                sumLock.release() # release lock when done
        p.print("Launching thread {} of {}".format(p.thread_num, p.num_threads))


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
    #infile1 = open('shakespeare1.txt',"r")
    linesToIterate = []
    
    with open('shakespeare1.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )
    with open('shakespeare2.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )
    with open('shakespeare3.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )
    with open('shakespeare4.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )
    with open('shakespeare5.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )
    with open('shakespeare6.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )
    with open('shakespeare7.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )
    with open('shakespeare8.txt',"r") as file:
        text = ""
        for line in file:
            text = text + line
        linesToIterate.append( text )

    
    wordlist = ["hate", "love", "death", "night", "sleep", "time",
                "henry", "hamlet", "you", "my", "blood", "poison", 
                "macbeth", "king", "heart", "honest"]

    #print(linesToIterate)
    #starting timer
    start = time.time()

    dictOfWords = dictOfItems(linesToIterate,wordlist)
    
    #stopping timer
    stop_time = time.time() - start

    print("time: ")
    print("%s seconds" % stop_time)
    print("\n")

    printResults(dictOfWords)

if __name__ == '__main__':
    # execute only if run as a script
    main()