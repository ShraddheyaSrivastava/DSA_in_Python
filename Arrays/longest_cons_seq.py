def lcs(lst):
    arr=set(lst)
    ans=0
    for val in arr:
        if val-1 not in arr:
            l=1
            while val+1 in arr:
                val=val+1
                l+=1
            ans=max(ans,l)
    return ans
             