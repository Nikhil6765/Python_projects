n=int(input('enter how many prime numbers you want : '))
n1=2
count=0
while True:
    is_prime=True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
        count=count+1

    if count==n:
        break
    n1+=1
    