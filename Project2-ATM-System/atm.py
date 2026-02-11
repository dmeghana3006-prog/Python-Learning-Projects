def check_balance(balance):
    print("Balance is: ",balance)
def withdrawal(balance):
    with_draw_amount=int(input("Enter the Amount: "))
    if with_draw_amount>0:
        if with_draw_amount<=balance:
            balance=balance-with_draw_amount
            print("Withdraw Successfully Completed")
        else:
            print("UnSufficent Balance")
    else:
        print("Invalid Amount. Enter Positive Amount")
    return balance
def deposit(balance):
    amount=int(input("Enter Your Amount: "))
    if amount>0:
        balance=balance+amount
        print("Amount Deposited Successfully!")
    else:
        print("Invalid Amount. Enter Positive Amount")
    return balance
def main():
    balance=1000
    while True: 
        print("1. Check Balance")
        print("2. WithDrawal")
        print("3. Deposit")
        print("4. Exit")
        option=int(input("Enter Your Choice: "))
        if option==4:
            print("Thanks for Visiting our ATM")
            break
        elif option==1:
            check_balance(balance)
        elif option==3:
           balance=deposit(balance)
        elif option==2:
            balance=withdrawal(balance)
        else:
            print("Invalid Option")
if __name__ == "__main__":
    main()
