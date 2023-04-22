def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

if __name__ == '__main__':
    number = int(input('Enter the number \n'))
    fac = factorial(number)
    print(fac)


""""
Wrong approach, just tried.

def factorial_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        count = 0
        for n in range(1,8):
            print(n)
            count += (n) * (n-1) * (n-2) * (n-3) * (n-4) * (n-5)
        return count

print(factorial_number(7))

"""
