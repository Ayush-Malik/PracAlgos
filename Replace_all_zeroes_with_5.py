num = int(input("Enter a number : "))

def reverse(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev

def transform_zeroes_to_5(num):
    x = 1
    y = 0
    while num != 0:
        if num % 10 == 0 :
            y = 10 * y + 5
        else:
            y = 10 * y + (num % 10)
        num = num // 10
        x = x * 10
    return reverse(y)


print(transform_zeroes_to_5(num))