list=[1,2,2,1,1]
def majorityElement(nums):
    for val in nums:
        count=0
        for v in nums:
            if val==v:
                count+=1
        if count>len(nums)/2:
            return val
    return -1

print(majorityElement(list))