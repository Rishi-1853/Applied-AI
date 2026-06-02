Marks= int(input("Enter Marks: "))

if(Marks<=20 and Marks>=0):
    print("You are Not Pass and not eligible for Scholarship")
elif(Marks>20 and Marks<=40):
    print("You are Pass but not eligible for Scholarship")
elif(Marks>50 and Marks<=60):
    print("You are Pass but not Eligible")
else:
    print("You are Pass and Eligible for Scholarship")
