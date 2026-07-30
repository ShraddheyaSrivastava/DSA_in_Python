nums=[1,2,3,4]

def pro_arr(list):
    n=len(list)
    prefix=[1]*n
    for i in range(1,n):
        prefix[i]=prefix[i-1]*list[i-1]
    suffix=[1]*n
    for i in range(len(list)-2,-1,-1):
        suffix[i]=suffix[i+1]*list[i+1]

    ans=[1]*n
    for i in range(len(list)):
        ans[i]=prefix[i]*suffix[i]

    return ans

print(pro_arr(nums))
