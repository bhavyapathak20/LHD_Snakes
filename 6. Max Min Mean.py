def num():
    lis=[23,55,27,19]
    print("lis=[23,55,27,19]")
    print("1. Maximum value")
    print("2. Minimum value")
    print("3. Mean value")
    user=int(input("Enter your choice:"))
    if user==1:
        mx=max(lis)
        print("Maximum value is",mx)
    elif user==2:
        mn=min(lis)
        print("Minimum value is",mn)
    elif user==3:
        length=len(lis)
        for r in range(length):
            sum=0
            sum= sum+ int(lis[r])
        mean=sum/length
        print("Mean value is",mean)
num()
print("PROGRAM ENDED")
print("=============")
while True:
    ask=input("again? (y/n)")
    if ask=='y':
        num()
    else:
        print('THANKS FOR USING THE PROGRAM :)')
        break


