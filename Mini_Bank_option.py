class customer:
    '''this  is a mini bank application'''
    bankname='nibuda bank'
    def __init__(self,name,balance=0.0): # constructor

        self.name=name #instance var
        self.balance=balance #instance var

    def deposit(self,amount):  #instance method
        self.balance=self.balance+amount
        print('after deposit , balance is : ',self.balance)

    def withdrawl(self,amount):
        if amount>self.balance:
            print('insufficient fund')
        else:
            self.balance=self.balance-amount
            print('after withdraw, balance :',self.balance)


print('Welcome to :',customer.bankname)
name=input('Enter Your Name : ')
c=customer(name)
while True:
    print('d-Deposit \n w- withdraw \n e-exit')
    option=input('choose your option : ')
    if option.lower()=='d':
        amount=float(input('enter amount to deposit : '))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('enter amount to withdraw : '))
        c.withdrawl(amount)

    elif option.lower()=='e':
        print('thanks for banking')
        break

    else:
        print('your option is invalid , please choose valid option')
        






