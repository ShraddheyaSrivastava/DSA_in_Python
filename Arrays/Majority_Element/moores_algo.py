arr=[1,2,2,1,1]

def majorityElement(nums: list[int])->int|None :
    ans=nums[0]
    count=1
    if not nums :
        return None
    for i in range(1,len(nums)):
        if count==0:
            ans=nums[i]
            count=1
        elif nums[i]==ans:
            count+=1
        else:
            count-=1
         

    count=sum(1 for val in nums if val==ans)
    if count > len(nums) // 2:
        return ans
    return None

print(majorityElement(arr))
