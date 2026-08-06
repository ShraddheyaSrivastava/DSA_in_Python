height=[1,8,6,2,5,4,8,3,7]

def max_water(col):
    st=0
    end=len(col)-1
    max_vol=0
    while st<end:
        h=min(col[st],col[end])
        w=end-st
        area=h*w
        max_vol=max(area,max_vol)
        # we will always move smaller column as it is controlling volume
        if col[st]<col[end]:
            st+=1
        else:
            end-=1

    return max_vol
    
print(max_water(height))
