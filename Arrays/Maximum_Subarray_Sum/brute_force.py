array=[3,-4,5,4,-1,7,-8]
def mx_sum(arr):
    maximum=float("-inf")
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            maximum=max(maximum,sum)
   
    return maximum
    
print(mx_sum(array))
    
    
  
    
 # sum of subarray with maximum sum


# subarray is a continuos part of an array