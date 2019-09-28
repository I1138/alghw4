# algorithms hw 4
import enum
import random


def main():
    tree = bsTree(10)
    for i in range(10):
        tree.insert(random.randint(0, 20))
    tree.printTree()
    return


class color(enum.Enum):
    RED = enum.auto()
    BLACK = enum.auto()

###############################################################################
# NODE
###############################################################################


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
        return self.rightChild

###############################################################################
# BS-Tree
###############################################################################


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

    def insert(self, data):
        currNode = self.root
        pastNode = None
        while currNode != self.Nil:
            pastNode = currNode
            if currNode.getData() <= data:
                currNode = currNode.getRightChild()
            else:
                currNode = currNode.getLeftChild()
        # deal with empty tree
        if self.Nil.getParent() == self.Nil:
            self.root = node(data, self.Nil, self.Nil, self.Nil)
            self.Nil.setLeftChild(self.root)
            self.Nil.setRightChild(self.root)
            self.Nil.setParent(self.root)
        elif pastNode.data <= data:
            pastNode.setRightChild(node(data, pastNode, self.Nil, self.Nil))
        else:
            pastNode.setLeftChild(node(data, pastNode, self.Nil, self.Nil))

    def delete(self):
        return

    def search(self, value, currNode=None):
        # make sure node passed is not nill
        if currNode is None:
            currNode = self.root

        # Search for value
        while currNode.data != value and currNode != self.Nil:
            # value will be less than or greater
            # return None if value is not found before nill node
            if (currNode.data < value):
                currNode = currNode.leftChild
            else:
                currNode = currNode.rightChild
        # don't return nil
        if currNode == self.Nil:
            currNode = None
        return currNode

    def printTree(self, indent=" ", currNode=None):
        if currNode is None:
            currNode = self.root
        print(indent, currNode.getData(), sep='')
        if currNode.getLeftChild() != self.Nil:
            self.printTree(indent+"<", currNode.getLeftChild())
        if currNode.getRightChild() != self.Nil:
            self.printTree(indent+">", currNode.getRightChild())
        return

    # Need to double check algorithm
    def transplant(self, unplantNode, plantNode):
        if (unplantNode.parent == self.Nil):
            self.root = plantNode
        elif (unplantNode == unplantNode.parent.leftChild):
            unplantNode.parent.leftChild = plantNode
        else:
            unplantNode.parent.rightChild = plantNode
        plantNode.parent = unplantNode.parent
        return

    # returns nil if no predecessor found
    def predecessor(self, startNode):
        # if has left sub tree
        if startNode.getLeftChild() != self.Nil:
            maxNode = self.maximum(startNode.getLeftChild())
        # else, look up tree for node w/ successor startNode
        else:
            maxNode = startNode.getParent()
            while maxNode != self.Nil and startNode == maxNode.getLeftChild():
                startNode = maxNode
                maxNode = maxNode.getParent()
        return maxNode

    # returns nil if no successor found
    def successor(self, startNode):
        if startNode.getRightChild() != self.Nil:
            minNode = self.minimum(startNode.getRightChild())
        else:  # look up tree for node w/ predecessor startNode
            minNode = startNode.getParent()
            while minNode != self.Nil and startNode == minNode.getRightChild():
                startNode = minNode
                minNode = minNode.getParent()
        return minNode

    def minimum(self, startNode=None):
        if startNode is None:
            startNode = self.root
        # while left child is not nill node, continue left
        if startNode != self.Nil:
            while (startNode.leftChild != self.Nil):
                startNode = startNode.leftChild
        return startNode

    def maximum(self, startNode=None):
        if startNode is None:
            startNode = self.root
        # while right child is not nill node, continue right
        if startNode != self.Nil:
            while (startNode.rightChild != self.Nil):
                startNode = startNode.rightChild
        return startNode


class rbTree(bsTree):
    def leftRotate(self, pivotNode=None):
        # check inputs
        if pivotNode is None:
            pivotNode = self.root
        rotateNode = None

        # check node we expect to rotate
        if pivotNode.rightChild != self.Nil:
            rotateNode = pivotNode.rightChild
        else:
            return

        # exchange pointers
        rotateNode.parent = pivotNode.parent
        pivotNode.parent = rotateNode
        pivotNode.rightChild = self.Nil
        rotateNode.leftChild = pivotNode

        # end condition for if pivot node is left or right child
        if pivotNode == pivotNode.parent.leftChild:
            rotateNode.parent.leftChild = rotateNode
        else:
            rotateNode.parent.rightChild = rotateNode
        return

    def rightRotate(self, pivotNode=None):
        # check inputs
        if pivotNode is None:
            pivotNode = self.root

        rotateNode = None

        # check node we expect to rotate
        if pivotNode.leftChild != self.Nil:
            rotateNode = pivotNode.leftChild
        else:
            return

        # exchange pointers
        rotateNode.parent = pivotNode.parent
        pivotNode.parent = rotateNode
        pivotNode.leftChild = self.Nil
        rotateNode.rightChild = pivotNode

        # end condition for if pivot node is left or right child
        if pivotNode == pivotNode.parent.leftChild:
            rotateNode.parent.leftChild = rotateNode
        else:
            rotateNode.parent.rightChild = rotateNode
        return


if __name__ == '__main__':
    main()
