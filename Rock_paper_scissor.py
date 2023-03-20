import time
import random

name=input('enter your name : ')

print('~ Welcome',name,'to the Rock-Paper-Scissor Game !!!')
Cchoice=['rock','paper','scissor']

while True:

    user_win,comp_win=0,0
    for i in range(1,4):
        print('Round',i,'starts !')            
        print('Please choose your option :')        
        print('1.Rock','2.paper','3.scissor',sep="\n")
        user_choice=int(input())
        time.sleep(2)
        
        if user_choice==1:
            user_choice='rock'
            print('you selected rock')

        elif user_choice==2:
            user_choice='paper'
            print('you selected paper')
        
        elif user_choice==3:
            user_choice='scissor'
            print('you selected scissor')
        else:
            print('invald input please try again')
            break

        comp_choice=random.choice(Cchoice)
        if comp_choice=='rock':
            print('computer choosed rock')
        elif comp_choice=='paper':
            print('computer choosed paper')
        elif comp_choice=='scissor':
            print('computer choosed scissor')
        
        time.sleep(2)

        if user_choice==comp_choice:
            print('tie!')
            user_win+=1
            comp_win+=1
        
        elif (user_choice=='paper' and comp_choice=='rock') or (user_choice=='rock' and comp_choice=='scissor') or (user_choice=='scissor' and comp_choice=='paper'):
            print(name,'wins!!!')
            user_win=user_win+1
        else:
            print('computer wins!!!')
            comp_win+=1

    print()
    time.sleep(3)

    if user_win>comp_win:
        print(name,'Wins the Game!!!')
    elif user_win<comp_win:
        print('computer wins he game!!!')
    else:
        print('match is tie!!!')
    
    user=input('Do you want to play again [yes/no] ? ')
    if user.lower()=='no':
        break

      
    

