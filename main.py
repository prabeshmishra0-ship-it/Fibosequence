def main():
    count = int(input("Enter the number of Fibonacci numbers: "))

    a = 0
    b = 1

    for i in range(count):
        print(a)
        a, b = b, a + b

main()