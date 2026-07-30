nums=[1,2,3,4]

def product_arr(list:list[int])->list[int]:
    n=len(list)
    full_pro=1
    ans=[1]*n
    for val in list:
        full_pro*=val

    for i in range(len(list)):
        ans[i]=full_pro//list[i]

    return ans
        


def pro_array(list:list[int])->list[int]:
    ans=[]
    for val in list:
        pro=1
        for v in list:  #without using // operator
            if v!=val:
                pro*=v
        ans.append(pro)
    return ans



print(product_arr(nums))
print(pro_array(nums))