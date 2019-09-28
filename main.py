# algorithms hw 4
import enum


def main():
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
        return self.leftChild

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

    def leftRotate(self, pivotNode = None):
        #check inputs
        if pivotNode is None:
            pivotNode = self.root

        #set rotateing node
        rotateNode = pivotNode.getRightChild()

        #turn rotateNode's left subtree into pivotNode's right subtree
        pivotNode.setRightChild(rotateNode.getLeftChild())
        if rotateNode != self.Nil:
            rotate.leftChild.setParent(pivotNode)

        #link pivotNode's parent to rotateNode
        rotateNode.setParent(pivotNode.getParent())
        if pivotNode.parent == self.nil:
            self.root = rotateNode
        elif pivotNode == pivotNode.getParent().getLeftChild():
            pivotNode.parent.setLeftChild(rotateNode)
        else:
            pivotNode.parent.setRightChild(rotateNode)

        #link pivotNode's parent to pivotNode
        rotateNode.setLeftChild(pivotNode)
        pivotNode.setParent(rotateNode)
        return

    def rightRotate(self, pivotNode = None):
        #check inputs
        if pivotNode is None:
            pivotNode = self.root

        #set rotateing node
        rotateNode = pivotNode.getLeftChild()

        #turn rotateNode's left subtree into pivotNode's right subtree
        pivotNode.setLeftChild(rotateNode.getRightChild())
        if rotateNode != self.Nil:
            rotateNode.rightChild.setParent(pivotNode)

        #link pivotNode's parent to rotateNode
        rotateNode.setParent(pivotNode.getParent())
        if pivotNode.parent == self.nil:
            self.root = rotateNode
        elif pivotNode == pivotNode.getParent().getRightChild():
            pivotNode.parent.setRightChild(rotateNode)
        else:
            pivotNode.parent.setLeftChild(rotateNode)

        #link pivotNode's parent to pivotNode
        rotateNode.setRightChild(pivotNode)
        pivotNode.setParent(rotateNode)
        return

    def insert(self):
        return

    def delete(self):
        return

    def search(self, value, currNode=None):
        # make sure node passed is not nill
        if currNode is None:
            currNode = self.root

        # Search for value
        while (currNode.data != value):
            # value will be less than or greater
            # return None if value is not found before nill node
            if (currNode.data < value):
                if(currNode.leftChild == self.Nil):
                    return None
                else:
                    currNode = currNode.leftChild
            else:
                if(currNode.rightChild == self.Nil):
                    return None
                else:
                    currNode = currNode.rightChild
        return currNode

    def printTree(self, indent=" ", currNode=None):
        if currNode is None:
            currNode = self.root
        print(indent + currNode.getData())
        if currNode.getLeftChild() != self.Nil:
            self.printTree(indent+" ", currNode.getLeftChild())
        if currNode.getRightChild() != self.Nil:
            self.printTree(indent+" ", currNode.getRightChild())
        return

    #Need to double check algorithm
    def transplant(self, unplantNode = self.root, plantNode = self.Nil):
        if (unplantNode.parent == self.Nil):
            self.root = plantNode
        elif (unplantNode == unplantNode.parent.leftChild):
            unplantNode.parent.leftChild = plantNode
        else:
            unplantNode.parent.rightChild = plantNode
        plantNode.parent = unplantNode.parent
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
