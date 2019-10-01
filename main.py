# algorithms hw 4
import enum
import random


def main():
    tree = rbTree(10)
    data = []
    for i in range(10):
        data.append(random.randint(0, 20))
        tree.insert(data[i])
        tree.printTree()
        checkTree(tree, tree.root)
        print()
    tree.printTree()
    print(tree.minimum().getData())
    print(tree.successor(tree.minimum()).getData())
    print(tree.maximum().getData())
    print(tree.predecessor(tree.maximum()).getData())
    checkTree(tree, tree.root)
    return


def checkTree(tree, currNode):
    if currNode == tree.Nil:
        return 1
    if currNode.parent.leftChild != currNode and currNode.parent.rightChild != currNode:
        print("child unclaimed by parent confusion on", currNode.data, "and parent", currNode.parent.data)
    if currNode.leftChild != tree.Nil and currNode.leftChild.parent != currNode:
        print("left child of parent", currNode.data, "does not recognize parent")
    if currNode.rightChild != tree.Nil and currNode.rightChild.parent != currNode:
        print("right child of parent", currNode.data, "does not recognize parent")
    if currNode.getColor() == color.RED and currNode.getParent().getColor() == color.RED:
        print("red node with red parent at ", currNode.data)
    leftBlackHeight = checkTree(tree, currNode.leftChild)
    rightBlackHeight = checkTree(tree, currNode.rightChild)
    if leftBlackHeight != rightBlackHeight:
        print("Black heights uneven at", currNode.data)
        # force unevenness up the rest of the tree
        blackHeight = -10
    else:
        blackHeight = leftBlackHeight
    if currNode.getColor() == color.BLACK:
        blackHeight += 1
    return blackHeight


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

    def delete(self, deleteNode):
        # single or no child cases
        if deleteNode.getLeftChild() == self.Nil:
            self.transplant(deleteNode, deleteNode.getRightChild())
        elif deleteNode.getRightChild() == self.Nil:
            self.transplant(deleteNode, deleteNode.getLeftChild())
        # two child cases
        else:
            successor = self.successor(deleteNode)
            # successor is removed from parent
            if successor.getParent() != deleteNode:
                self.transplant(successor, successor.getRightChild())
                successor.setRightChild(deleteNode.getRightChild())
                successor.getRightChild().setParent(successor)
            # successor is not removed from parent
            self.transplant(deleteNode, successor)
            successor.setLeftChild(deleteNode.getLeftChild())
            successor.getLeftChild().setParent(successor)

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

    def transplant(self, unplantNode, plantNode):
        if (unplantNode.parent == self.Nil):
            self.root = plantNode
        elif (unplantNode == unplantNode.parent.leftChild):
            unplantNode.parent.leftChild = plantNode
        else:
            unplantNode.parent.rightChild = plantNode
        plantNode.parent = unplantNode.parent

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

###############################################################################
# RB-Tree
###############################################################################


# rbTree inherits from bsTree
class rbTree(bsTree):
    def printTree(self, indent=" ", currNode=None):
        if currNode is None:
            currNode = self.root
        print(indent, currNode.getData(), ' ', currNode.getColor().name, sep='')
        if currNode.getLeftChild() != self.Nil:
            self.printTree(indent+"<", currNode.getLeftChild())
        if currNode.getRightChild() != self.Nil:
            self.printTree(indent+">", currNode.getRightChild())

    def insert(self, data):
        currNode = self.root
        pastNode = None
        while currNode != self.Nil:
            pastNode = currNode
            if currNode.getData() <= data:
                currNode = currNode.getRightChild()
            else:
                currNode = currNode.getLeftChild()
        insertNode = node(data, pastNode, self.Nil, self.Nil, color.RED)
        if pastNode.data <= data:
            pastNode.setRightChild(insertNode)
        else:
            pastNode.setLeftChild(insertNode)
        self.insertFixUp(insertNode)

    def isRightChild(self, currNode):
        if currNode.parent.rightChild == currNode:
            return True
        return False

    def leftRotate(self, pivotNode=None):
        # set rotateing node
        rotateNode = pivotNode.getRightChild()

        # turn rotateNode's left subtree into pivotNode's right subtree
        pivotNode.setRightChild(rotateNode.getLeftChild())
        if rotateNode != self.Nil:
            rotateNode.leftChild.setParent(pivotNode)
        # link pivotNode's parent to rotateNode
        rotateNode.setParent(pivotNode.getParent())
        if pivotNode.parent == self.Nil:
            self.root = rotateNode
            self.Nil.setLeftChild(self.root)
            self.Nil.setRightChild(self.root)
        elif pivotNode == pivotNode.getParent().getLeftChild():
            pivotNode.parent.setLeftChild(rotateNode)
        else:
            pivotNode.parent.setRightChild(rotateNode)

        # link pivotNode's parent to pivotNode
        rotateNode.setLeftChild(pivotNode)
        pivotNode.setParent(rotateNode)

    def rightRotate(self, pivotNode):
        # set rotateing node
        rotateNode = pivotNode.getLeftChild()

        # turn rotateNode's left subtree into pivotNode's right subtree
        pivotNode.setLeftChild(rotateNode.getRightChild())

        if rotateNode != self.Nil:
            rotateNode.rightChild.setParent(pivotNode)

        # link pivotNode's parent to rotateNode
        rotateNode.setParent(pivotNode.getParent())
        if pivotNode.parent == self.Nil:
            self.root = rotateNode
            self.Nil.setLeftChild(self.root)
            self.Nil.setRightChild(self.root)
        elif pivotNode == pivotNode.getParent().getRightChild():
            pivotNode.parent.setRightChild(rotateNode)
        else:
            pivotNode.parent.setLeftChild(rotateNode)

        # link pivotNode's parent to pivotNode
        rotateNode.setRightChild(pivotNode)
        pivotNode.setParent(rotateNode)
        return

    def insertFixUp(self, currNode):
        # text z = currnode
        while currNode.getParent().getColor() == color.RED:
            if currNode.getParent().getParent().getLeftChild() == currNode.getParent():
                uncle = currNode.getParent().getParent().getRightChild()
                if uncle.getColor() == color.RED:
                    currNode.getParent().setColor(color.BLACK)
                    uncle.setColor(color.BLACK)
                    currNode.getParent().getParent().setColor(color.RED)
                    currNode = currNode.getParent().getParent()
                else:
                    if currNode == currNode.getParent().getRightChild():
                        currNode = currNode.getParent()
                        self.leftRotate(currNode)
                    currNode.getParent().setColor(color.BLACK)
                    currNode.getParent().getParent().setColor(color.RED)
                    self.rightRotate(currNode.getParent().getParent())
            else:
                uncle = currNode.getParent().getParent().getLeftChild()
                if uncle.getColor() == color.RED:
                    currNode.getParent().setColor(color.BLACK)
                    uncle.setColor(color.BLACK)
                    currNode.getParent().getParent().setColor(color.RED)
                    currNode = currNode.getParent().getParent()
                else:
                    if currNode == currNode.getParent().getLeftChild():
                        currNode = currNode.getParent()
                        self.rightRotate(currNode)
                    currNode.getParent().setColor(color.BLACK)
                    currNode.getParent().getParent().setColor(color.RED)
                    self.leftRotate(currNode.getParent().getParent())
            self.root.setColor(color.BLACK)

    def delete(self, deleteNode):
        currNode = deleteNode
        currNodeOrigColor = currNode.getColor()
        moveNode = None
        if deleteNode.getLeftChild() == self.Nil:
            moveNode = deleteNode.getRightChild()
            self.transplant(deleteNode, deleteNode.getRightChild())
        elif deleteNode.getRightChild() == self.Nil:
            moveNode = deleteNode.getLeftChild()
            self.transplant(deleteNode, deleteNode.getLeftChild())
        else:
            currNode = self.minimum(deleteNode.getRightChild())
            currNode.setColor(currNodeOrigColor)
            moveNode = currNode.getRightChild()
            if currNode.getParent() == deleteNode:
                moveNode.getParent() == currNode
            else:
                self.transplant(currNode, currNode.getRightChild())
                currNode.setRightChild(deleteNode.getRightChild())
                currNode.getRightChild().setParent(currNode)
            self.transplant(deleteNode, currNode)
            currNode.setLeftChild(deleteNode.getLeftChild())
            currNode.getLeftChild().setParent(currNode)
            currNode.setColor(deleteNode.getColor())
        if currNodeOrigColor == color.BLACK:
            self.deleteFixup(moveNode)

    def deleteFixup(self, currNode):
        moveNode = None
        while currNode != self.root and currNode.getColor() == color.BLACK:
            if not self.isRightChild(currNode):
                moveNode = currNode.getParent().getRightChild()
                if moveNode.getColor() == color.RED:
                    moveNode.setColor(color.BLACK)
                    currNode.getParent().setColor(color.RED)
                    self.leftRotate(currNode.getParent())
                    moveNode = currNode.getParent().getRightChild()
                if moveNode.getLeftChild().getColor() == color.BLACK and moveNode.getRightChild().getColor() == color.BLACK:
                    moveNode.setColor(color.RED)
                    currNode = currNode.getParent()
                else:
                    if moveNode.getRightChild().getColor() == color.BLACK:
                        moveNode.getLeftChild().setColor(color.BLACK)
                        moveNode.setColor(color.RED)
                        self.rightRotate(moveNode)
                    moveNode.setColor(currNode.getParent().getColor())
                    currNode.getParent().setColor(color.BLACK)
                    self.leftRotate(currNode.getParent())
                    currNode = self.Root
            else: # TODO: adjust left right
                moveNode = currNode.getParent().getRightChild()
                if moveNode.getColor() == color.RED:
                    moveNode.setColor(color.BLACK)
                    currNode.getParent().setColor(color.RED)
                    self.leftRotate(currNode.getParent())
                    moveNode = currNode.getParent().getRightChild()
                if moveNode.getLeftChild().getColor() == color.BLACK and moveNode.getRightChild().getColor() == color.BLACK:
                    moveNode.setColor(color.RED)
                    currNode = currNode.getParent()
                else:
                    if moveNode.getRightChild().getColor() == color.BLACK:
                        moveNode.getLeftChild().setColor(color.BLACK)
                        moveNode.setColor(color.RED)
                        self.rightRotate(moveNode)
                    moveNode.setColor(currNode.getParent().getColor())
                    currNode.getParent().setColor(color.BLACK)
                    self.leftRotate(currNode.getParent())
                    currNode = self.Root

if __name__ == '__main__':
    main()
