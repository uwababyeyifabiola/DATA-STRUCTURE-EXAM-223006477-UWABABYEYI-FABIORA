from collections import deque
from datetime import datetime, timedelta
import json
import os

class InvoiceItem:
    def __init__(self, description, hours, rate):
        self.description = description
        self.hours = float(hours)
        self.rate = float(rate)
        self.amount = self.hours * self.rate

    def to_dict(self):
        return {
            'description': self.description,
            'hours': self.hours,
            'rate': self.rate,
            'amount': self.amount
        }

class Invoice:
    def __init__(self, invoice_number, client_name, date=None):
        self.invoice_number = invoice_number
        self.client_name = client_name
        self.date = date if date else datetime.now().strftime('%Y-%m-%d')
        self.items = []
        self.total_amount = 0.0
        self.due_date = (datetime.strptime(self.date, '%Y-%m-%d') + 
                        timedelta(days=30)).strftime('%Y-%m-%d')

    def add_item(self, item):
        self.items.append(item)
        self.total_amount += item.amount

    def to_dict(self):
        return {
            'invoice_number': self.invoice_number,
            'client_name': self.client_name,
            'date': self.date,
            'due_date': self.due_date,
            'items': [item.to_dict() for item in self.items],
            'total_amount': self.total_amount
        }

class InvoiceGenerator:
    def __init__(self):
        self.invoices = deque(maxlen=100)  # Store last 100 invoices
        self.current_invoice_number = self._load_last_invoice_number()

    def _load_last_invoice_number(self):
        try:
            if os.path.exists('invoices.json'):
                with open('invoices.json', 'r') as f:
                    data = json.load(f)
                    if data:
                        return max(int(invoice['invoice_number']) 
                                 for invoice in data)
        except Exception:
            pass
        return 1000  # Start from 1000 if no previous invoices

    def create_invoice(self, client_name):
        self.current_invoice_number += 1
        invoice = Invoice(self.current_invoice_number, client_name)
        return invoice

    def add_invoice(self, invoice):
        self.invoices.append(invoice)
        self._save_invoices()

    def get_recent_invoices(self, count=5):
        return list(self.invoices)[-count:]

    def get_invoice_by_number(self, invoice_number):
        for invoice in self.invoices:
            if invoice.invoice_number == invoice_number:
                return invoice
        return None

    def _save_invoices(self):
        with open('invoices.json', 'w') as f:
            json.dump([invoice.to_dict() for invoice in self.invoices], 
                     f, indent=2)

def generate_invoice_text(invoice):
    """Generate a formatted text representation of the invoice"""
    text = f"""
INVOICE
{'=' * 50}
Invoice Number: {invoice.invoice_number}
Date: {invoice.date}
Due Date: {invoice.due_date}

Bill To:
{invoice.client_name}

Items:
{'-' * 50}
{"Description":<30} {"Hours":>8} {"Rate":>8} {"Amount":>8}
{'-' * 50}
"""
    
    for item in invoice.items:
        text += f"{item.description:<30} {item.hours:>8.2f} {item.rate:>8.2f} {item.amount:>8.2f}\n"
    
    text += f"""
{'-' * 50}
{"Total Amount:":<46} {invoice.total_amount:>8.2f}

Payment Terms: Net 30
Please make payment by: {invoice.due_date}
"""
    return text

# Example usage
def main():
    # Initialize the generator
    generator = InvoiceGenerator()
    
    # Create a new invoice
    invoice = generator.create_invoice("Tech Corp")
    
    # Add items to the invoice
    items = [
        InvoiceItem("Web Development", 10, 75),
        InvoiceItem("UI/UX Design", 5, 60),
        InvoiceItem("Project Management", 3, 85)
    ]
    
    for item in items:
        invoice.add_item(item)
    
    # Add invoice to the generator
    generator.add_invoice(invoice)
    
    # Print the invoice
    print(generate_invoice_text(invoice))
    
    # Get recent invoices
    recent_invoices = generator.get_recent_invoices()
    print(f"\nRecent invoices: {len(recent_invoices)}")
    for inv in recent_invoices:
        print(f"Invoice #{inv.invoice_number} - {inv.client_name}: ${inv.total_amount:.2f}")

if __name__ == "__main__":
    main()
