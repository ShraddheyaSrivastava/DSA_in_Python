def sum3(arr):
    n=len(arr)
    ans=[]
    s=set()
    for i in range(n):
        e1=arr[i]
        for j in range(i+1,n):
            e2=arr[j]
            for k in range(j+1,n):
                e3=arr[k]
                if e1+e2+e3==0:
                    grp=sorted([e1,e2,e3])
                    if tuple(grp) not in s:
                        s.add(tuple(grp))
                        ans.add(grp)
    return ans
