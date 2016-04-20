# AVL Trees, by Elizabeth Feicke

class AVLNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None
        self.balanceFactor = 0


def less_than(x,y):
    return x < y

class AVLTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.less = less


    def height(self, node):
        if node:
            return 1 + max(self.height(node.left), self.height(node.right))
        else:
            return -1

    def leftRotate(self, n):
        y = n.right
        n.right = y.left
        if y.left:
            y.left.parent = n
        y.parent = n.parent
        if n.parent == None:
            self.root = y
        elif n == n.parent.left:
            n.parent.left = y
        else:
            n.parent.right = y
        y.left = n
        n.parent = y
        n.balanceFactor = n.balanceFactor + 1 - min(y.balanceFactor, 0)
        y.balanceFactor = y.balanceFactor + 1 + max(n.balanceFactor, 0)


    def rightRotate(self, n):
        x = n.left
        n.left = x.left
        if x.right:
            x.right.parent = n
        x.parent = n.parent
        if n.parent == None:
            self.root = x
        elif n == n.parent.right:
            n.parent.right = x
        else:
            n.parent.left = x
        x.right = n
        n.parent = x
        ##Min and max might need to be switched, doubt it though - blake
        n.balanceFactor = n.balanceFactor + 1 - min(x.balanceFactor, 0)
        x.balanceFactor = x.balanceFactor + 1 + max(n.balanceFactor, 0)



    def rebalanceTree(self,n):
        if n.balanceFactor < 0:
            if n.right.balanceFactor > 0:
                self.rightRotate(n.right)
                self.leftRotate(n)
            else:
                self.leftRotate(n)
        elif n.balanceFactor > 0:
            if n.left.balanceFactor < 0:
                self.leftRotate(n.left)
                self.rightRotate(n)
            else:
                self.rightRotate(n)

    def updateBalance(self,n):
        if n.balanceFactor > 1 or n.balanceFactor < -1:
            self.rebalanceTree(n)
            return
        if n.parent:
            if n.left:
                n.parent.balanceFactor += 1
            elif n.right:
                n.parent.balanceFactor -= 1
            if n.parent.balanceFactor != 0:
                self.updateBalance(n.parent)




    # takes value, returns node with key value
    def insert(self, k):
        z = AVLNode(k)
        y = None
        x = self.root
        while x:
            y = x
            if self.less(z.key,x.key):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
            self.updateBalance(self.root)
            return self.root
        elif self.less(z.key,y.key):
            y.left = z
            self.updateBalance(y.left)
            return y.left
        else:
            y.right = z
            self.updateBalance(y.right)
            return y.right



    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):
        x = self.search(n.key)
        if x != None:
            if x.right != None:
                return self.tree_minimum(x.right)
            return self.greatest_ancestor(x)


    def tree_minimum(self, n):
        if n.left:
            return self.tree_minimum(n.left)
        else:
            return n

    def greatest_ancestor(self, n):
        p = n.parent
        if p and n == p.right:
            return self.greatest_ancestor(p)
        return p
    # return the node with the largest key smaller than n.key
    def predecessor(self, n):
        x = self.search(n.key)
        if x.left:
            return self.tree_max(x.left)
        else:
            return self.least_ancestor(n)

    def least_ancestor(self, n):
        p = n.parent
        if p and n == p.left:
            return self.least_ancestor(p)
        return p

    def tree_max(self, n):
        if n.right:
            return self.tree_max(n.right)
        else:
            return n
    # takes key returns node
    # can return None
    def search(self, k):
        n = self.root
        while n:
            if n.key == k:
                return n
            if self.less(k, n.key):
                if n.left:
                    n = n.left
                else:
                    return None
            else:
                if n.right:
                    n = n.right
                else:
                    return None


    # takes node, returns node
    def delete_node(self, node):
        n = self.search(node.key)
        if n.left == None:
            self.transplant(n, n.right)
        elif n.right == None:
            self.tranplant(n, n.left)
        else:
            newStart = self.tree_minimum(n.right)
            if newStart.parent != n:
                self.tranplant(newStart, newStart.right)
                newStart.right = n.right
                newStart.right.parent = newStart
            self.transplant(n, newStart)
            newStart.left = n.left
            newStart.left.parent = newStart
        self.updateBalance(n.parent)
        return n

    def transplant(self, orig, new):
        if orig.parent == None:
            self.root = new
        elif orig == orig.parent.left:
            orig.parent.left = new
        else:
            orig.parent.right = new
        if new != None:
            new.parent = orig.parent
