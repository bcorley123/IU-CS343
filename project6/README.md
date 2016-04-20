#Project 6 - Hash Tables in Compression
_____________________________________________________________

##Hashtable.py

This file implements hashtables using the chaining method of collision avoidance and table doubling to control the load factor and space consumption of the hashtable.

###__init__

Records how many slots are use, the size of the table and fills in the slots with the passed dictionary.

###__getitem__

Returns the item from the slot based on the given key.

###__setitem__

Appends a key value pair to the end of the list of a slot. If the table is too big we double it.

###__delitem__ 

Deletes an item in the table. It pops off an item at a given location in the array. Halves a table when it gets too small.  

###Keys

Returns a list of all the keys in the table.

###countKeys

Gets a count of all the keys in the table.

###tableDouble

Instantiates a new table with twice the size. Readjusts slots.

###tableHalf

Divides table size in half. Readjusts slots.

###Times

It took us about 4 hours to write the code and another 4 hours to debug. 