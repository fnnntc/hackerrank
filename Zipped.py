# Enter your code here. Read input from STDIN. Print output to STDOUT
students,subjects = map(int,input().split())
grades=[]
for subject in range(subjects):
    grade=list(map(float,input().split()))
    grades+=[grade]
x= ((list(zip(*grades))))
for i in x:
    print(sum(i)/subjects)


