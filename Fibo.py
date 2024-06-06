## Fibonacci number using Recurrsion

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1)+fibo(n-2)

if __name__ == "__main__":
    n = int(input("Enter number: "))
    print(fibo(n))