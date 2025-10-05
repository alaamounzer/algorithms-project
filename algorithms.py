def factorial(n):
    i = 1       
    result = 1  
    while i <= n:
        result *= i
        i += 1  
    return result

print(factorial(5))  


def find_max(numbers):
    max = numbers[0] 
    for num in numbers[1:]:  
        if num > max:
            max = num
    return max

print(find_max([3, 7, 2, 9, 5]))

  