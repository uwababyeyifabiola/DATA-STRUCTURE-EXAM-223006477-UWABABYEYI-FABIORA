#Create Circular Linked List to manage a fixed number of orders in the invoice generator for freelancers.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0  
        self.capacity = 0  
    
    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def is_empty(self):
        return self.head is None
    
    def is_full(self):
        return self.size == self.capacity
    
    def add_order(self, data):
        if self.is_full():
            raise OverflowError("Circular Linked List is full")
        
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head 
        else:
            self.tail.next = new_node 
            self.tail = new_node  
            self.tail.next = self.head  
        
        self.size += 1
    
    def remove_order(self):
        if self.is_empty():
            raise IndexError("Circular Linked List is empty")
        
        removed_data = self.head.data
        if self.head == self.tail:  
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next 
            self.tail.next = self.head  
        
        self.size -= 1
        return removed_data
    
    def display_orders(self):
        if self.is_empty():
            print("No orders in the list")
            return
        
        current = self.head
        print("Orders in Circular Linked List:")
        for _ in range(self.size):
            print(current.data, end=" -> ")
            current = current.next
        print("(back to head)")


order_list = CircularLinkedList()
order_list.set_capacity(5)  


order_list.add_order("Order #101")
order_list.add_order("Order #102")
order_list.add_order("Order #103")
order_list.add_order("Order #104")

order_list.display_orders()  


print("\nProcessing orders:")
print(order_list.remove_order())  
print(order_list.remove_order())  

order_list.display_orders()  


order_list.add_order("Order #105")
order_list.add_order("Order #106")

order_list.display_orders()  