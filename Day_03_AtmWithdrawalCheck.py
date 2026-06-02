Balance= float(input("Enter Your Account Balance: "))
Withdrawal_amount= float(input("Enter the amount you want to withdraw: "))

if Withdrawal_amount <= Balance:
    print("Withdrawal Successful.")
    print("Remaining Balance: ", Balance - Withdrawal_amount)
else:
    print("Insufficient Funds.")