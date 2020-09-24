a=[1,1,2,2,4,4,5,5,5]

a.sort()
i=0
l=len(a)
cnt=0
res=0
tmp=[]
while i<l:

    if len(tmp)==0:
        tmp.append(a[i])
        i+=1
    
    elif abs(a[i]-tmp[0])<=1:
        tmp.append(a[i])
        i+=1
    else:
        if len(tmp)>res:
            res=len(tmp)
        tmp=[]
        tmp.append(a[i])
        i+=1
if len(tmp)>res:
    res=len(tmp)
print(res)
    
