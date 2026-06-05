# Step 1: Define the structure of a single Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Implement the Queue using Front and Rear pointers
class LinkedQueue:
    def __init__(self):
        self.front = None  # Points to the element ready to leave
        self.rear = None   # Points to the last element added
        self._size = 0     # Track the total number of items

    # Enqueue: Add an element to the back (rear)
    def enqueue(self, data):
        new_node = Node(data)
        
        # If the queue is empty, new node becomes both front and rear
        if self.rear is None:
            self.front = self.rear = new_node
            self._size += 1
            return
            
        # Otherwise, link it to the end and update the rear pointer
        self.rear.next = new_node
        self.rear = new_node
        self._size += 1

    # Dequeue: Remove and return the element from the front
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
            
        popped_data = self.front.data  # Save data to return
        self.front = self.front.next    # Shift front pointer to the next node
        
        # If front becomes None, the queue is completely empty
        if self.front is None:
            self.rear = None
            
        self._size -= 1
        return popped_data

    # Peek: Look at the front element without removing it
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    # Check if the queue is empty
    def is_empty(self):
        return self.front is None

    # Get the current size of the queue
    def size(self):
        return self._size

    # Display the queue from Front to Rear
    def display(self):
        curr = self.front
        print("Front -> ", end="")
        while curr is not None:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("Rear")