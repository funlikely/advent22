"""
    Fun times with monkeys and problem 11
"""


class Monkey:

    def __init__(self, items, operation, operand, test, targets):
        self.items = items
        """list of worry levels, e.g., [23, 45] represents 2 items with worry levels 23 and 45"""
        self.operation = operation
        """should be an enum, but will be something in {'add', 'multiply', 'square'} """
        self.operand = operand
        """for 'add' and 'multiply' we need an operand"""
        self.test = test
        """an integer for the divisibility test"""
        self.targets = targets
        """which two monkeys to send things at after the divisibility test"""
