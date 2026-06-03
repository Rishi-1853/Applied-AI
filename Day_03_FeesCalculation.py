Tuition_Fees= float(input("Enter the Tuition Fees: "))
Hostel_Fees= float(input("Enter the Hostel Fees: "))
Food_Fees= float(input("Enter Food Fees: "))
Uniform_Fees= float(input("Enter the Uniform Fees: "))
Total_Fees= Tuition_Fees + Hostel_Fees + Food_Fees + Uniform_Fees

print("The Total Fees is: ", Total_Fees)

Scholarship_Discount= Total_Fees * 0.15
Final_Fees= Total_Fees - Scholarship_Discount

print("The Final Fees after Scholarship Discount is: ", Final_Fees)