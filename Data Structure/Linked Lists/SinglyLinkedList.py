# Create Node
# Create Linked List
# Add node to Link List
# Print  a Link List
# Add Fist Node
# Iterate to find last node for adding a new node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None
        
    # Get length of a Linked List
    def length(self):
        position = 0
        currNode = self.head
        while currNode.next is not None:
            position +=1
            currNode = currNode.next
        return position
    
    # Insert at the end of Linked List
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next = newNode
    
    #Insert at specific location using index
    def insertAt (self,newNode,position):
        if position == 0:
            self.insertHead(newNode)
            return
        elif position > self.length():
            print("Entering at wrong place")
            return
        currPos = 0
        currNode = self.head
        while currNode.next is not None:
            if currPos == position:
                break
            currPos +=1
            prevNode  = currNode
            currNode = currNode.next
        prevNode.next = newNode
        newNode.next = currNode
        
    # Insert at the starting of Linked List        
    def insertHead(self,newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode
    
    # Print a message if List is empty
    def printList(self):
        if self.head is None:
            print("List is Empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
    
    # Delete head of a Linked List
    def delHead(self):
        tempNode = self.head
        tempNode = tempNode.next
        self.head = tempNode
        del tempNode
    
    # Delete from end of Linked List
    def delEnd(self):
        lastNode = self.head.next
        while lastNode.next is not None:
            prevNode = lastNode
            lastNode = lastNode.next
        prevNode.next = None
        del lastNode