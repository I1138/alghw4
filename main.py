# algorithms hw 4
import enum


def main():
    return


class color(enum.Enum):
    RED = enum.auto()
    BLACK = enum.auto()


# node class, has parent, children, and data
class node:
    def __init__(self, data, nodeParent, nodeLeftChild, nodeRightChild, color=color.BLACK):
        self.data = data
        self.parent = nodeParent
        self.leftChild = nodeLeftChild
        self.rightChild = nodeRightChild
        self.color = color

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setParent(self, nodeParent):
        self.parent = nodeParent

    def getParent(self):
        return self.parent

    def setLeftChild(self, nodeLeftChild):
        self.leftChild = nodeLeftChild

    def getLeftChild(self):
        return self.leftChild

    def setRightChild(self, nodeRightChild):
        self.rightChild = nodeRightChild

    def getRightChild(self):
        return self.leftChild


class bsTree:
    def __init__(self, data=None):
        # create nil first
        self.Nil = node(None, None, None, None)
        # make root second, so that nil can be set as parent and child
        self.root = node(data, self.Nil, self.Nil, self.Nil)
        # update nil
        self.Nil.setParent(self.root)
        self.Nil.setRightChild(self.root)
        self.Nil.setLeftChild(self.root)

    def insert(self):
        return

    def delete(self):
        return

    def search(self):
        return

    def printTree(self, indent=" ", currNode=None):
        if currNode is None:
            currNode = self.root
        print(indent + currNode.getData())
        if currNode.getLeftChild() != self.Nil:
            self.printTree(indent+" ", currNode.getLeftChild())
        if currNode.getRightChild() != self.Nil:
            self.printTree(indent+" ", currNode.getRightChild())
        return

    def transplant(self):
        return

    def predecessor(self, startNode):
        if startNode != self.Nil and startNode.getLeftChild() != self.Nil:
            minNode = self.minimum(startNode.getLeftChild())
        else:
            minNode = startNode
        return minNode

    def successor(self, startNode):
        if startNode != self.Nil and startNode.getRightChild() != self.Nil:
            minNode = self.minimum(startNode.getRightChild())
        else:
            minNode = startNode
        return minNode

    def minimum(self):
        return

    def maximum(self):
        return
