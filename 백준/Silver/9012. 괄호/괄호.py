# stack
class Casual_Stack:
    def __init__(self):
        self.s = []

    def push(self, data):
        self.s.append(data)
    
    def pop(self):
        return self.s.pop()

    def is_empty(self):
        return len(self.s) == 0
    
    def peek(self):
        return "empty" if self.is_empty() else self.s[-1]
    
    def __str__(self):
        return str(self.s)
    

def valid(txt):
    b_stack = Casual_Stack()
    is_valid = True
    for b in txt:
        if b == "(":
            b_stack.push(b)
        else:
            if b_stack.is_empty():
                is_valid = False
                break
            else:
                if b_stack.pop() == "(":
                    continue
    if not b_stack.is_empty():
        is_valid = False

    return "YES" if is_valid else "NO"

# print(valid("(())())"))
T = int(input())
for i in range(T):
    print(valid(input()))