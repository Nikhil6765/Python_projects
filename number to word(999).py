n=int(input('enter number : '))


l1=[' ','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
l2=['','','tewenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']

if n==0:
    print('zero')
elif n<=19:
    print(l1[n])

elif n<=99:
    print(l2[n//10]+' '+l1[n%10])

elif n<=119:
    print('One Hundred'+' '+l1[n%100])

elif n<=199:
    print('one hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=219:
    print('two hundred'+' '+l1[n%100])

elif n<=299:
    print('two hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=319:
    print('three hundred'+' '+l1[n%100])

elif n<=399:
    print('three hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=419:
    print('four hundred'+' '+l1[n%100])

elif n<=499:
    print('four hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=519:
    print('five hundred'+' '+l1[n%100])

elif n<=599:
    print('five hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=619:
    print('six hundred'+' '+l1[n%100])

elif n<=699:
    print('six hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=719:
    print('seven hundred'+' '+l1[n%100])

elif n<=799:
    print('seven hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=819:
    print('eight hundred'+' '+l1[n%100])

elif n<=899:
    print('eight hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])

elif n<=919:
    print('nine hundred'+' '+l1[n%100])

elif n<=999:
    print('nine hundred'+' '+l2[(n%100)//10]+' '+l1[(n%100)%10])





