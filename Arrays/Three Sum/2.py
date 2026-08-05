def threeSum(nums: list[int]) -> list[list[int]]:
        n=len(nums)
        grp=set()
        for i in range(n):
            s=set()
            for j in range(i+1,n):
                tar=-(nums[i]+nums[j])
                if tar in s:
                    trip= tuple(sorted([nums[i],nums[j],tar]))
                    grp.add(trip)
                else:
                    s.add(nums[j])
        
        ans=list(list(trip) for trip in grp)
        return ans
arr=[-1,0,1,2,-1,-4]
print(threeSum( arr))