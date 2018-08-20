class LinkedNode:
    prv = None  # type: LinkedNode
    nxt = None  # type: LinkedNode
    data = None

    def __init__(self, d=None, p=None, n=None):
        self.data = d
        self.prv = p
        self.nxt = n

class LinkedList:
    root = None

    def __init__(self, r=None):
        self.root = r
        if self.root is not None:
            self.root.nxt = self.root
            self.root.prv = self.root

    def length(self):
        if self.root is None:
            return 0

        count = 1
        active_node = self.root
        while active_node.nxt is not self.root:
            count += 1
            active_node = active_node.nxt

        return count

    def insert(self, node, index=None):
        if index is None:
            if self.root is None:
                node.nxt = node
                node.prv = node
                self.root = node
                return
            self.root.prv.nxt = node
            node.prv = self.root.prv
            self.root.prv = node
            node.nxt = self.root
        else:
            a_node = self.root
            for idx in range(index):
                a_node = a_node.nxt
            a_node.prv.nxt = node
            node.prv = a_node.prv
            a_node.prv = node
            node.nxt = a_node
            if index is 0:
                self.root = node
