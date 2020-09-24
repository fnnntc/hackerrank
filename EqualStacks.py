'''h1=[3, 2, 1, 1, 1]
h2=[4,3,2]
h3=[1,1,4,1]'''
h1=[1,1,1,1,1]
h2=[3,2]
h3=[1,3,1]

s1,s2,s3=sum(h1),sum(h2),sum(h3)
if s1==s2 and s2==s3:
    return s1
m=max(s1,s2,s3)

while h1 or h2 or h3:
    if s1==m:
        x=h1.pop(0)
        s1-=x
    elif s2==m:
        x=h2.pop(0)
        s2-=x
    else: 
        x=h3.pop(0)
        s3-=x
    m=max(s1,s2,s3)
    if m==s1 and s1==s2 and s2==s3:
        break
print(m)