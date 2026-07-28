list=[1,2,2,1,1,2,3,2,2]

"""def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]"""

def majorityElement(nums):
    nums.sort()
    ans=nums[0] # as if there is only one element in the list then that is the majority element
    count=1
    for i in range(1,len(nums)):
        if nums[i]==nums[i-1]:
            count+=1
        else:
            count=1
        if count>len(nums)//2:
            ans=nums[i]
    return ans

print(majorityElement(list))