n = int(input("Enter Starting Number: "))
print(n)
if n < 0 or n == 0:
    print('Error! The number is not positive!')
else:
    while n != 1:
        if (n % 2 == 0):
            n = n/2
            print(n)
        else:
            n = (3 * n ) + 1
            print(n)

