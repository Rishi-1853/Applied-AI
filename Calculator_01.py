a= int(input("Enter 1st Number: "))
b= int(input("Enter 2nd Number: "))

Select= input("Enter any of +,-,*,/");

if Select == "+":
    result= a+b
    print ("The result is", a+b);

elif Select == "-":
    result= a-b
    print ("The result is", a-b);

elif Select == "*":
    result= a*b
    print ("The result is", a*b);

else:
    result= a/b
    print ("The result is", a/b);
    