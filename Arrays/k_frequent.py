def kf(arr,k):
    f={}
    ans=[]
    for val in arr:
        f[val]=f.get(val,0)+1
    fre=[]
    for val in f:
        fre.append([val,f[val]])
    fre.sort(key=lambda x:x[1] , reverse=True)
    for i in range(k):
        ans.append(fre[i][0])
    return ans
arr=[1,1,2,1,3,4,3,6,6,6,6,6,1]
print(kf(arr,3))
