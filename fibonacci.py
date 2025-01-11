def fibonacci(n):
    n1 = 0
    n2 = 1
    while(n>0):
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        n = n-1

fibonacci(1000)    