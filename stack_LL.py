class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedStack:
    def __init_(self):
        self.head = None
        self.length = 0


    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def peek(self):
        if self.is_empty():
            return None 
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.length 


    def display(self):
        curr = self.head
        print("Top->",end="")
        while curr is  not None:
            print(curr.data,end=" ->")
            curr = curr.next
        print("None")                        

