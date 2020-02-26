# Parallel-Computing-MapReduce
This assignment implements a parallel map-reduce design pattern. The program will search for a set of words:

hate, love, death, night, sleep, time, henry, hamlet, you, my, blood, poison, macbeth, king, heart, honest

among a set of documents that constitute the works of Shakespeare. 

The program counts the number of a specific words within a specific document and combine the individual word counts.It will output the total instances of all words and the counts for each individual word.

## Instructions
Run:
python mapreduce.py 

To change the number of threads used:
Change the number of threads in pymp.Parallel() in the code
to 1+ the number of threads you want to use to search

## Issues encountered:
1. When adding more than one thread, my code deadlocked.
2. Not all threads initialized were being used to calculate the search
3. Increasing threads increased the execution time per thread.

## How I overcame some problems:
1. I initialized the dictionary inside the parallel section
2. p.iterate() will use one thread to manage the other threads' scheduling
3. I was locking every word at a line to increase the count in the shared dictionary, probably queueing the threads, ended up creating a local dictionary per thread to add to the shared dictionary 

## Bugs in program:
No bugs

## How long it took me to complete this assignment:
The coding only took about an hour, however, so far it's taken a couple days and two office hour sessions with David to fix different python Parallel bugs

## Performance Measurements:
 Thread num - seconds:
     1 - 0.9s
     2 - 0.57s
     4 - 0.56s
     6 - 0.58s

## Increasing # of Threads:
Going from 1 to 2 threads almost halves the execution time. Adding more threads does not seem to affect the time, in fact adding 8 threads increase the average time of execution.

## Observations:
Doubling the threads from 1 to 2 decrease the parallel time by around half. The execution time seems to even out around the time. However, something interesting happened when using 8 threads. The avg. execution time increased by 0.1 s. this may be due to the firstly assigned threads finishing their job and being placed on hold waiting to be assigned another job until the thread manager finishes going down the queue of waiting threads. i.e. the job each thread is doing is shorter than the assignment of all waiting threads, ending up in extending execution times as threads are waiting to be assigned.

## Output of cpuInfoDump.sh:
Intel(R) Core(TM) i7-7560U CPU @ 2.40GHz 4 -- 36 -- 216
