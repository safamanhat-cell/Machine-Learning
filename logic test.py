# 1

# Function to reverse the digits of a number
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev
array = [12, 23, 54]
result = []
for num in array:
    result.append(reverse_number(num))
for num in result:
    print(num, end=" ")




# 2
n = 4
# for i in range(1, n + 1):
#     print("*" * i, end="")
#     print(" " * (2 * (n - i)), end="")
#     print("*" * i)
# for i in range(n, 0, -1):
#     print("*" * i, end="")
#     print(" " * (2 * (n - i)), end="")
#     print("*" * i)
#     print("*" * i, end="")
#     print(" " * (2 * (n - i)), end="")
#     print("*" * i)



    




    
