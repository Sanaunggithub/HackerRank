def pairs(k, arr):
    
    # num2 - num = k
    # num2 = k + num
    
    seen = set(arr)
    result = 0

    for num in seen:
        if num + k in seen:
            result  += 1

    return result

arr = [1, 5, 3, 4, 2]
k = 2
print(pairs(k, arr))