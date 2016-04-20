#Project 4 - DNA Sequence Alignment
_____________________________________________________________

##SEQ_ALIGN


Our DNA sequencing algorithm takes in two sequences and returns the two sequences in an optimally aligned manner.  

  To do so, we start by creating a dot board of size s1 X s2. We initialize it with all 0 values. We then fill in the top row and column with descending negative values. We then fill in the rest of the board using this heuristic.

*take a diag value plus a match, mismatch, or space value 

*take the top and left value plus gap penalty

*take the max value of the three and set the value

Now that we have our board, we can now iterate through the board and find the optimally aligned subsequence.

We start at the bottom right of the board and find the value to the top, left, and diagonal. If the diag is the greatest number. We append the matched numbers together. If not we instead append a ‘_’ to the string. We then return the value of the two newly created sequences.
