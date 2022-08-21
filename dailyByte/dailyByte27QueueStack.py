# Design a class to implement a stack using only a single queue. 
# Your class, QueueStack, should support the following stack methods: 
# push() (adding an item), pop() (removing an item), peek() (returning the 
# top value without removing it), and empty() (whether or not the stack is empty).

class QueueStack:
    def __init__(self):
        self.l = []
    def push(self, x):
        self.l.append(x)
    def pop(self, y):
        self.l.pop(y)
    def peek(self):
        return self.l[-1]
    def empty(self):
        if not self.l:
            print("It's empty")
        else:
            print("Not empty")
k = QueueStack()
k.push(4)
k.push(3)
k.push(1)
k.push(8)
k.empty()