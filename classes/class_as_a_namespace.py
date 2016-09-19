"""Explaining class-as-a-namespace notion
"""

class ClassAsANamespace:
    """Demo class-as-a-namespace
    """
    name1 = 'Hello, World!'
    name2 = 1
    name3 = [1, 2, 3]
    name4 = {
        'test': 'Hello, World!'
    }

# You cannot use the statement below, as name1 is inside
#   ClassAsANamespace's namespace. Uncomment it and see it running
# print(name1)

print(ClassAsANamespace.name1)
print(ClassAsANamespace.name2)
print(ClassAsANamespace.name3)
print(ClassAsANamespace.name4)

