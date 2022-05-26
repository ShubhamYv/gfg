def factorial(N):
    # code here
    fact = 1
    for i in range(2,N+1):
        fact = fact*i
    return str(fact)


def main():
    n= int(input())
    print(factorial(n))

if __name__ == '__main__':
    main()