# Parallel-Computing-MapReduce
This assignment implements a parallel map-reduce design pattern. The program will search for a set of words:

hate, love, death, night, sleep, time, henry, hamlet, you, my, blood, poison, macbeth, king, heart, honest

among a set of documents that constitute the works of Shakespeare. 

The programcount the number of a specific word within a specific document and combine the individual word counts.It will output the total instances of all words and the counts for each individual word

##Instructions
Run:
python mapreduce.py 

To change the number of threads used:
Change the number of threads in pymp.Parallel() in the code

##Issues encountered:
I began coding the assignment using one thread, and when it worked, I added another and came accross deadlock.

##How I overcame some problems:
Still trying to resolve deadlock issues.

##Bugs in program:
No bugs

##How long it took me to complete this assignment:
So far it's taken 3 hours. The longest part was figuring out the way I wanted to parse the text and look for the words.

##Performance Measurements:


##Increasing # of Threads:


##Observations:


##Output of cpuInfoDump.sh:
Intel(R) Core(TM) i7-7560U CPU @ 2.40GHz 4 -- 36 -- 216
