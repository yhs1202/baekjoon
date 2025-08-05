# queue
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front == None:
            current = Node(data)
            self.front = current
            self.rear = current
        else:
            current = Node(data)
            self.rear.next = current
            self.rear = current

    def dequeue(self):
        if self.front == None:
            return None
        else:
            current = self.front
            self.front = self.front.next
            return current.data
            
    def is_empty(self):
        return self.front == None
    
    def __str__(self):
        result = []
        current = self.front
        while current:
            result.append(current.data)
            current = current.next
            return str(result)
        
N = int(input())

q = Queue()
for i in range(1, N+1):
    q.enqueue(i)

while True:
    if q.front == q.rear:
        break
    q.dequeue()
    if q.front == q.rear:
        break
    q.enqueue(q.dequeue())
print(q.dequeue())