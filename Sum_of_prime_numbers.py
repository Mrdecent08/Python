low = int(input("Enter lower limit : "))
up = int(input("Enter upper limit : "))
for i in range(low,up):
    b = 0
    for j in range(1,i):
        if(i%j==0):
            b+=1
    if(b==1) :
        print(str(i) +" is a prime number")     