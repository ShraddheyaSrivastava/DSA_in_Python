nums=[1,2,3,4]

def pro_arr(list):
    n=len(list)
    ans=[1]*n
    prefix=1
    for i in range(1,n): #prefix loop
        
        """ans[i]=ans[i-1]*list[i-1]"""
        prefix=list[i-1]*prefix
        ans[i]*=prefix

    
    suffix=1
    for i in range(n-2,-1,-1): # suffix loop
        suffix=list[i+1]*suffix
        ans[i]*=suffix

    return ans



"""def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n

    # Store prefix products
    prefix = 1
    for i in range(n):
        ans[i] = prefix
        prefix *= nums[i]

    # Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= suffix
        suffix *= nums[i]

    return ans"""


print(pro_arr(nums))
        