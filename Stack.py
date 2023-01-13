class Stack(object):
    def __init__(self, length = 10):
        self.length = length
        self.stack = length*[None]

    def isEmpty(self):
        if len(self.stack) == 0:
            print("Stack Underflow")

    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            return self.stack.pop()

    def push(self, data):
        if len(self.stack) == self.length:
            self.resize()
        else:
            return self.stack.append(data)

    def peek(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            return self.stack[-1]

    def isFull(self):
        if len(self.stack) >= self.length:
            print("Stack Overflow")

    def size(self):
        return len(self.stack)

    def resize(self):
        newstack = list(self.stack)
        self.length = 2*self.length
        self.stack = newstack

objstack = Stack(1)
objstack.push(1)
objstack.push(2)
objstack.push(3)
objstack.push(4)
print(objstack.peek())
objstack.pop()
objstack.push(5)
objstack.push(6)
objstack.push(7)
print(objstack.peek())
objstack.pop()
objstack.pop()
print(objstack.peek())