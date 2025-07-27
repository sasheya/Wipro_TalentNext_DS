
import sys

# Write a program to accept two numbers as command line arguments and display their sum.
def sumOfNum():
    if len(sys.argv) != 3:
        print("Enter two numbers as command line arguments.")
        return
    else:
        print("Sum:", int(sys.argv[1]) + int(sys.argv[2]))

sumOfNum()


# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
def welcomeMsg():
    if len(sys.argv) < 2:
        print("Please provide a welcome message as a command line argument.")
        return
    else:
        filename = sys.argv[0]
        message = " ".join(sys.argv[1:])
        print(f'{filename}, {message}')

welcomeMsg()

# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primeSum():
    numbers = [int(x) for x in sys.argv[1:]]

    if len(numbers) != 10:
        print("Please provide 10 numbers as command line arguments.")
    else:
        primeSum = sum(num for num in numbers if isPrime(num))
        print("Sum of prime numbers:", primeSum)

primeSum()

