from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        

    def push(self, x):
        n = len(self.q1)
        self.q1.append(x)
        for _ in range(n):
            self.q1.append(self.q1.popleft())
        

    def pop(self):
        return self.q1.popleft()
        

    def top(self):
        return self.q1[0]
        

    def empty(self):
        return len(self.q1)==0
        