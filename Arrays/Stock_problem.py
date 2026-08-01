prices=[7,1,5,3,6,4]
def max_pro(price:list[int])->int:
    best_buy=price[0]
    max_profit=0
    for i in range(1,len(price)):    
        max_profit=max(max_profit,(price[i]-best_buy))
        best_buy=min(best_buy,price[i])
    if max_profit<=0:
        return 0
    else:
        return max_profit

print(max_pro(prices))