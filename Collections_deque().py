# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
c = int(input())
d = deque()
for i in range(c):
    cmd = input().split()
    if len(cmd)==1:
        cmd="d.{}()".format(cmd[0])
        exec(cmd)
    elif len(cmd)==2:
        cmd="d.{}({})".format(cmd[0],cmd[1])
        exec(cmd)

for i in d:
    print(i,end=" ")
