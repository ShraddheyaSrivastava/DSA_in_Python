def sum3(arr):
    arr.sort()
    ans=[]
    n=len(arr)
    for i in range(n-2):
        st=i+1
        end=n-1
        tar=-arr[i]
        if arr[i]>0:
            break
        if arr[i]==arr[i-1] and i>0:
            continue
        if arr[i]+arr[i+1]+arr[i+2]>0:
            break
        if arr[i]+arr[n-1]+arr[n-2]<0:
            continue
        while st<end:
            val=arr[st]+arr[end]
            if val==tar:
                ans.append([arr[i],arr[st],arr[end]])
                st+=1
                end-=1
                while st<end and arr[st]==arr[st-1]:
                        st+=1
                while st<end and arr[end]==arr[end+1]:
                        end-=1
            elif val>tar:
                end-=1
            else:
                st+=1
    return ans
