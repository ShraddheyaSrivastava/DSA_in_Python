arr=[0,1,3,4,5,6,7,8,9]

def missing_num(arr):
    n=len(arr)
    real_sum=sum(arr)
    norm_sum=n*(n+1)//2
    return (norm_sum-real_sum)

def miss(arr):
    xor=len(arr)
    for i in range(len(arr)):
        xor^=arr[i]
        xor^=i
    return xor

def ms(arr):
    ans=len(arr)
    for i,num in enumerate(arr):
        ans^=i^num
    return ans

print(missing_num(arr))
print(miss(arr))
print(ms(arr))