    cnt = [0]*6
    for el in arr:
        cnt[el]+=1
    return(cnt.index(max(cnt)))

