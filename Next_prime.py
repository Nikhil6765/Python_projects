def next_prime(n):
    while True:
        n=n+1
        for i in range(2,n):
            if n%i==0:
                break
        
        else:
            return n


number=int(input("Enter the number to get next prime number : "))
print(next_prime(number))
