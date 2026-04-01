class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Test 1 - basic dry run
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(2)
print(ms.getMin())   # 2
ms.pop()
print(ms.getMin())   # 3
print(ms.top())      # 7

# Test 2 - single element
ms2 = MinStack()
ms2.push(10)
print(ms2.getMin())  # 10
print(ms2.top())     # 10

# Test 3 - pushing same value
ms3 = MinStack()
ms3.push(1)
ms3.push(1)
print(ms3.getMin())  # 1
ms3.pop()
print(ms3.getMin())  # 1