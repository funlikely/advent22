"""
    Fun times with monkeys and problem 11
"""


class Monkey:

    def __init__(self, items, op, opnum, test, targets):
        self.items = items
        """list of worry levels, e.g., [23, 45] represents 2 items with worry levels 23 and 45"""
        self.test = test
        """an integer for the divisibility test"""
        self.targets = targets
        """which two monkeys to send things at after the divisibility test"""
        self.activity_counter = 0

        # self.operation = operation
        # these lambdas are failing. new ones overwrite old ones . . . so let's go back to a simpler method
        """a lambda for the worry operation, like lambda x: x + 3"""
        self.op = op
        self.opnum = opnum

    def operate(self, x):
        if self.op == "square":
            return x * x
        elif self.op == "multiply":
            return x * self.opnum
        else:
            return x + self.opnum
