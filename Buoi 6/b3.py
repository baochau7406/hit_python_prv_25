class myStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_Empty(self):
        return len(self.stack) == 0

    def is_Full(self):
        return len(self.stack) == self.capacity
    
    def pop(self):
        if self.is_Empty():
            print("Stack is empty")
            return None
        return self.stack.pop()

    def push(self, value):
        if self.is_Full():
            print("Stack is full!")
            return
        self.stack.append(value)

    def top(self):
        if self.is_Empty():
            return None
        else:
            return self.stack[-1]
        
    def printStack(self):
        if self.is_Empty():
            print("Stack rỗng.")
            return
        print("Stack:")
        for i in reversed(self.stack):
            print(i)


stack = myStack(5)
stack.push(1)
stack.push(2)
stack.printStack()
print(stack.is_Full())
print(stack.pop())
print(stack.top())