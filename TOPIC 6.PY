class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []  # List of child nodes
    
    def add_child(self, child_node):
        """Adds a child node to the current node."""
        self.children.append(child_node)
    
    def display(self, level=0):
        """Displays the tree structure."""
        print(" " * (level * 4) + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)


# Example Usage in Invoice Generator
# Root Node: Freelance Invoices
root = TreeNode("Freelance Invoices")

# Level 1: Projects
project1 = TreeNode("Project A")
project2 = TreeNode("Project B")
root.add_child(project1)
root.add_child(project2)

# Level 2: Clients under Project A
client1 = TreeNode("Client X")
client2 = TreeNode("Client Y")
project1.add_child(client1)
project1.add_child(client2)

# Level 3: Invoices under Client X
invoice1 = TreeNode("Invoice #101 - Paid")
invoice2 = TreeNode("Invoice #102 - Unpaid")
client1.add_child(invoice1)
client1.add_child(invoice2)

# Level 3: Invoices under Client Y
invoice3 = TreeNode("Invoice #103 - Paid")
client2.add_child(invoice3)

# Level 2: Clients under Project B
client3 = TreeNode("Client Z")
project2.add_child(client3)

# Level 3: Invoices under Client Z
invoice4 = TreeNode("Invoice #104 - Unpaid")
client3.add_child(invoice4)

# Display the hierarchical tree structure
print("Invoice Hierarchy:")
root.display()