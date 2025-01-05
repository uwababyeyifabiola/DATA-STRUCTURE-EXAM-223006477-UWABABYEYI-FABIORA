from collections import deque

class InvoiceDeque:
    def __init__(self):
        self.deque = deque()
    
    def add_invoice_front(self, invoice):
        """Add an invoice to the front of the deque."""
        self.deque.appendleft(invoice)
        print(f"Added to front: {invoice}")
    
    def add_invoice_rear(self, invoice):
        """Add an invoice to the rear of the deque."""
        self.deque.append(invoice)
        print(f"Added to rear: {invoice}")
    
    def remove_invoice_front(self):
        """Remove and return an invoice from the front."""
        if not self.deque:
            raise IndexError("No invoices to process at the front")
        invoice = self.deque.popleft()
        print(f"Processed from front: {invoice}")
        return invoice
    
    def remove_invoice_rear(self):
        """Remove and return an invoice from the rear."""
        if not self.deque:
            raise IndexError("No invoices to process at the rear")
        invoice = self.deque.pop()
        print(f"Processed from rear: {invoice}")
        return invoice
    
    def peek_front(self):
        """View the invoice at the front without removing it."""
        if not self.deque:
            raise IndexError("No invoices to view at the front")
        return self.deque[0]
    
    def peek_rear(self):
        """View the invoice at the rear without removing it."""
        if not self.deque:
            raise IndexError("No invoices to view at the rear")
        return self.deque[-1]
    
    def is_empty(self):
        """Check if the deque is empty."""
        return len(self.deque) == 0
    
    def display(self):
        """Display all invoices in the deque."""
        print("Current invoices in the deque:")
        for invoice in self.deque:
            print(invoice)
