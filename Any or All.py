# Enter your code here. Read input from STDIN. Print output to STDOUT
N=input()
set_N=input().split()
print(all(int(x)>=0 for x in set_N) and any(x==x[::-1] for x in set_N))
