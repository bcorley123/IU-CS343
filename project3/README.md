#Intersecting Lines and Search Trees

##BST.py
This file contains 5 main methods and a few helper functions. It can insert, find the successor and predecessor, search and delete node. Theoretically the worst case running time for all of these functions should be O(n). 


##AVL.py
This file contain the same functions as BST but altered in a way that balances the tree with every step. Each node has a balance factor that updates with every changed made to the tree. If the balance factor is too high or too low then the tree is rebalance using rotations. Theoretically the worst case running time for all of these functions should be O(log n). However in practices we have found the BST to run faster. Which surprised us.
