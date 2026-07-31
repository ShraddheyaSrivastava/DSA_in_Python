array=[3,-4,5,4,-1,7,-8]
def max_subarray_sum(arr):
    max_sum=float("-inf")
    sum=0
    for val in arr:
        sum+=val
        max_sum=max(max_sum,sum)
        if sum<0:
            sum=0
    return max_sum

print(max_subarray_sum(array))
