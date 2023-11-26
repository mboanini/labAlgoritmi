# nodo ABR
class ABRNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None


# ABR
class ABR:
    def __init__(self):
        self.Nil = ABRNode(0)
        self.Nil.left = None
        self.Nil.right = None
        self.root = self.Nil
        self.node_read = 0
        self.node_written = 0

    def get_node_read(self):
        return self.node_read

    def get_node_written(self):
        return self.node_written

    # ricerca
    def ABR_search(self, key):
        return self.ABRfindNode(self.root, key)

    def ABRfindNode(self, currentNode, key):
        if currentNode is None:
            return False
        elif key == currentNode.key:
            self.node_read += 1
            return True
        elif key < currentNode.key:
            self.node_read += 1
            return self.ABRfindNode(currentNode.left, key)
        elif key > currentNode.key:
            self.node_read += 1
            return self.ABRfindNode(currentNode.right, key)

    # insert
    def ABR_insert(self, z):
        y = None
        x = self.root
        while x is not None:
            self.node_read += 1
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        self.node_written += 1
        return z