x=int(input("Enter the first  number : "))
y=int(input("Enter the  second number : "))
z=int(input("Choose what operation you want -> \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exponent \n"))

if(z==1):
    print(" The result is " , x+y)
elif(z==2):
    print(" The result is " , x-y)
elif(z==3):
    print(" The resut is " , x*y)
elif(z==4):
    print(" The result is " , x/y)
elif(z==5):
    print(" The result is " , x**y)
else:
    print("Wrong choice .... !")

