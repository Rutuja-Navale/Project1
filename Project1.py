name = input("Enter your name: ")          # 1. take name
pin = input("Enter PIN: ")      # 2. Enter PIN

balance = 5000  # 3. starting balance

print(f"\nWelcome {name}...")  # 4. greet user

while True:  # 5. keep menu running until user exits
    print("\n 1. Check Balance \n 2. Deposit \n 3. Withdraw \n 4. Exit \n")
    choice = input("Enter choice: ")  # 6. user picks option

    if choice == "1":  # 7. check balance
        print("Available balance: $", balance)

    elif choice == "2":  # 8. deposit
        amt = float(input("Enter amount to deposit: "))
        balance += amt  # add money
        print("Deposited! New balance: $", balance)

    elif choice == "3":  # 9. withdraw
        amt = float(input("Enter amount to withdraw: "))
        if amt > balance:  # 10. check if enough money
            print("Not enough balance")
        else:
            p = input("Enter PIN to withdraw money: ")  # 11. ask PIN
            if p == pin:  # 12. check PIN
                balance -= amt  # 13. deduct money
                print("Money withdrawn. New balance: $", balance)  # 14. success
            else:
                print("Wrong PIN! Transaction failed")  # 15. wrong PIN

    elif choice == "4":  # 16. exit option
        print("Thank you", name...)
        break  # 17. stop loop

    else:  # 18. invalid input
        print("Invalid choice, Try Again...")