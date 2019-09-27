# algorithms hw 4


def main():
    return


# node class, has parent, children, and data
class node:
    def __init__(self, data, nodeParent, nodeLeftChild, nodeRightChild):
        self.data = data
        self.parent = nodeParent
        self.leftChild = nodeLeftChild
        self.rightChild = nodeRightChild

    def getData(self):
        return self.data

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
