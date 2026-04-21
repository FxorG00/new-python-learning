def sum_all(*num) :
    ans=0
    for var in num :
        ans+=var
    return ans
print(sum_all(10,20,30,40))