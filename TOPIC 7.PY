class Invoice:
    def __init__(self, invoice_id, priority):
        self.invoice_id = invoice_id
        self.priority = priority  # Priority level (e.g., higher number = higher priority)
    
    def __repr__(self):
        return f"Invoice({self.invoice_id}, Priority: {self.priority})"


def insertion_sort(invoices):
    """
    Sorts a list of Invoice objects based on their priority using Insertion Sort.
    """
    for i in range(1, len(invoices)):
        key = invoices[i]
        j = i - 1
        # Move elements of invoices[0..i-1] that are greater than key.priority
        # to one position ahead of their current position
        while j >= 0 and invoices[j].priority < key.priority:
            invoices[j + 1] = invoices[j]
            j -= 1
        invoices[j + 1] = key


# Example Usage
invoices = [
    Invoice("Invoice #101", 2),  # Low priority
    Invoice("Invoice #102", 5),  # High priority
    Invoice("Invoice #103", 3),  # Medium priority
    Invoice("Invoice #104", 1),  # Lowest priority
    Invoice("Invoice #105", 4),  # High-Medium priority
]

print("Before Sorting:")
for invoice in invoices:
    print(invoice)

# Sort invoices by priority
insertion_sort(invoices)

print("\nAfter Sorting (Descending Priority):")
for invoice in invoices:
    print(invoice)
