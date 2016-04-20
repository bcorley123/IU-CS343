#Project 5 - Compression using Priority Queues
_____________________________________________________________

##Heap.py

This file implements a priority queue using the minimum heap data structure in order
compress data using Huffman encoding.

###Minimum

Simple. Grab the first elm in the array.

###Insert

Takes a value. Starts by inserting a large number into the array. Then it puts the value into
the array and swaps until the heap property is satisfied.

###Extract_min

Starts by grabbing the minimum value. Then moves that last value to the front. Then fixes the heap.

###Min_heapify 

Fixes the heap. It does that by first taking an index i, then finding the left and right child of the heap.
It then finds if it's child is smaller. If one is, it swaps the values and recursively calls itself.

###Build_min_heap

Builds a heap from an array by calling min_heapify in the middle of the array.




###Times

It took us about 4 hours to write the code and another 4 hours to debug. Our biggest problem we were comparing the 
wrong types of data in the insert method.

Last week book work took around 3 hours, not including the reading. Which might have taken 3 hours.
Not sure though.