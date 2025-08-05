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
        
N, K = map(int, input().split())
q = Queue()
result = "<"
for i in range(1, N+1):
    q.enqueue(i)

while not q.is_empty():
    for _ in range(K-1):
        q.enqueue(q.dequeue())

    result += (str(q.dequeue()) + ", ")

result = result[:-2] + ">"
print(result)