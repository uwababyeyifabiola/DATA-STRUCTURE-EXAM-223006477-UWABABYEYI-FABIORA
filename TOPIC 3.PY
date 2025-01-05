class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum size of the queue
        self.queue = [None] * capacity  # Initialize queue with None values
        self.front = -1  # Index of the front item
        self.rear = -1  # Index of the rear item
    
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front
    
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Circular Queue is full")
        if self.is_empty():  # First element being added
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity  # Move rear to the next position
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        item = self.queue[self.front]
        self.queue[self.front] = None  # Optional: Clear the slot for visualization
        if self.front == self.rear:  # Queue becomes empty after this operation
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity  # Move front to the next position
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Circular Queue is empty")
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Circular Queue is empty")
        else:
            print("Circular Queue contents:")
            index = self.front
            while True:
                print(self.queue[index], end=" ")
                if index == self.rear:
                    break
                index = (index + 1) % self.capacity
            print()


# Example Usage in Invoice Generator
# Create a circular queue with a capacity of 5
invoice_queue = CircularQueue(5)

# Enqueue invoices
invoice_queue.enqueue("Invoice #101")
invoice_queue.enqueue("Invoice #102")
invoice_queue.enqueue("Invoice #103")
invoice_queue.enqueue("Invoice #104")

invoice_queue.display()  # Display the current state of the queue

# Process invoices
print("\nProcessing invoices:")
print(invoice_queue.dequeue())  # Process Invoice #101
print(invoice_queue.dequeue())  # Process Invoice #102

# Add more invoices
invoice_queue.enqueue("Invoice #105")
invoice_queue.enqueue("Invoice #106")

invoice_queue.display()  # Display the updated state of the queue

# Process remaining invoices
print("\nProcessing remaining invoices:")
while not invoice_queue.is_empty():
    print(invoice_queue.dequeue())