def sort_color(arr):
    lw=0
    mid=0
    hg=len(arr)-1
    while mid<=hg:
        if arr[mid]==0:
            arr[mid],arr[lw]=arr[lw],arr[mid]
            lw+=1
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[hg]=arr[hg],arr[mid]
            hg-=1
        else:
            mid+=1
    return arr