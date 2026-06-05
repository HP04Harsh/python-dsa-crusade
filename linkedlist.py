class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node    

    def display():

        current = self.head

        while current is not None:
            print(current.data,end="")
            current = current.next
        print("None")    

    def insert_at_position(self,data,position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return 

        curr = self.head
        for i in range(position-1):
            if curr is None:
                raise IndexError("Position out of bounds")    
            curr = curr.next

        if curr is None:
            raise IndexError("Position out of bounds")

        new_node.next = curr.next
        curr.next = new_node            


        def delete_value(self,value):
            if self.head is None:
                return


            if self.head.data == value:
                self.head = self.head.nextreturn


            curr = self.head
            while curr.next is not None:
                if curr.next.data is not None:
                    if curr.next.data == value:
                        curr.next = curr.next.next
                        return
                    curr = curr.next 
            print("Value not found in the list.")                    