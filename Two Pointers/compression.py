def compress(chars):
    i=0
    n=len(chars)
    idx=0
    while i<n:
        count=0
        ch=chars[i]
        while i<n and ch==chars[i]:
            count+=1
            i+=1
        """if count==1:
            chars[idx]=ch
            idx+=1
        else:
            chars[idx]=ch
            idx+=1
            c=str(count)
            for val in c:
                chars[idx]=val
                idx+=1"""
        chars[idx]=ch
        idx+=1
        if count>1:
            c=str(count)
            for val in c:
                chars[idx]=val
                idx+=1
        
    return idx

