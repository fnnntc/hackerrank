# Enter your code here. Read input from STDIN. Print output to STDOUT
class Que:
    def __init__(self):
        self.orderedStack = []
        self.reversedStack = []

    def reverseAndPop(self):
        if not self.reversedStack:
            while self.orderedStack:
                self.reversedStack.append(self.orderedStack.pop())
        if self.reversedStack:
            return self.reversedStack.pop()
    
    def deque(self):
        self.reverseAndPop()
    
    def enque(self, data):
        self.orderedStack.append(data)

    def printFront(self):
        front = self.reverseAndPop()
        print(front)
        self.reversedStack.append(front)


q = Que()
t = int(input())
for i in range(t):
    cmd = list(map(int,input().split()))
    if cmd[0] == 1:
        q.enque(cmd[1])
    elif cmd[0] == 2:
        q.deque()
    elif cmd[0] == 3:
        q.printFront()
