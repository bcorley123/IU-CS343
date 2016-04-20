from stack import ArrayStack

class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None

def less_than(x,y):
    return x < y

class BinarySearchTree:
    def __init__(self, root = None, less=less_than):
        self.root = root
        self.parents = True
        self.less = less

    # takes value, returns node with key value
    def insert(self, k):
        z = BSTNode(k)
        y = None
        x = self.root
        while x != None:
            y = x
            if self.less(z.key,x.key):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
            return self.root
        elif self.less(z.key,y.key):
            y.left = z
            return y.left
        else:
            y.right = z
            return y.right

    # takes node, returns node
    # return the node with the smallest key greater than n.key
    def successor(self, n):
        x = self.search(n.key)
        #x = n
        if x != None:
            if x.right:
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
            return self.least_ancestor(x)

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
