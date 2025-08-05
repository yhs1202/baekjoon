import re
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


def check(txt):
    def valid(txt):
        b_stack = Casual_Stack()
        is_valid = True
        for b in txt:
            if b == "(" or b == "[":
                b_stack.push(b)
                # print("push", b_stack)
            else:
                if b_stack.is_empty():
                    is_valid = False
                    break
                else:
                    if b == ")" and b_stack.pop() == "(":
                        # print("pop1", b_stack)
                        continue
                    elif b == "]" and b_stack.pop() == "[":
                        # print("pop2", b_stack)
                        continue
                    else:
                        is_valid = False
                        break
        if not b_stack.is_empty():
            is_valid = False
        return is_valid
    txt = re.findall(r'\(|\)|\[|\]', txt)
    return "yes" if valid(txt) else "no"

# print(check("So when I die (the [first] I will see in (heaven) is a score list)."))
# print(check("[ first in ] ( first out )."))
# print(check("Half Moon tonight (At least it is better than no Moon at all]."))
# print(check("A rope may form )( a trail in a maze."))
# print(check("Help( I[m being held prisoner in a fortune cookie factory)]."))
# print(check("([ (([( [ ] ) ( ) (( ))] )) ])."))
# print(check(" ."))

while True:
    txt = input()
    if txt == ".":
        break
    else:
        print(check(txt))