#  Implement Queue and Queue to manage data in the invoice generator for freelancers.
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)  
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)  
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]  
    
    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)  
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()  
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]  
    
    def size(self):
        return len(self.items)

invoice_queue = Queue()
invoice_queue.enqueue("Invoice #101")
invoice_queue.enqueue("Invoice #102")
invoice_queue.enqueue("Invoice #103")

print("Processing invoices:")
while not invoice_queue.is_empty():
    print(f"Processing {invoice_queue.dequeue()}")

action_stack = Stack()
action_stack.push("Added Invoice #101")
action_stack.push("Edited Invoice #102")
action_stack.push("Deleted Invoice #103")

print("\nUndoing actions:")
while not action_stack.is_empty():
    print(f"Undoing action: {action_stack.pop()}")