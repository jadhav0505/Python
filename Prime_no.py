num=input("Enter the no:")
count=0
if num>1:
    for i in range(1,num+1):
         if (num%1)==0:
            count=count+1
    if count==2:
        print("Number is Prime")
    else:
        print("Number is not prime")
