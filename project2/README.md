=======Analysis========

When looking at our graph the time complexity of our flood1 function is roughly f(n)= n. 
For our second graph is roughly f(n)= log n.


Flood takes the dictionary color-of-tiles that contains the color value of each title, an array flooded-list of tiles already flooded , and the screen size. Our function is called at every step in the game. When it is called it iterates through all of the tiles in the flooded list. During that it checks to see if the color of tile matches the newly changed tile. If it does and is not already in the flooded-list, then that tile is added to the flooded-list.


====Execution Time of Flood=====

We had two variations of our flood function. In the first one we just used the flooded_list in its normal array form to search through. Our second variations differed slightly, but happened to make a big difference. It turns out that if you turn the list into a set the run time greatly improves.

For our first version we were getting a linear run time of about f(n)=kn where k is a constant greater than 1. We expected this value since we are only going through the flooded list at most once. The fact that we had to go through each title in the flooded-list contributed to the n run time, hence why it runs in time n. For 2500 the time scale to about 100. (times1.xls)

For our second version we changed the flooded-list to a set. This changed the run time to about f(n)= log n. We did not expect to receive the results we did. I�m not quite sure how the set data structure works, but I will keep this in mind for the next time I have to iterate through a large list. For 2500 the time scale to about .99. Which we can see is a drastic difference from the first one.(times2.xls)
