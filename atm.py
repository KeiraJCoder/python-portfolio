def cash_machine():
    balance = 5000
    attempts = 0

    def pin_func():
        nonlocal attempts
        pin = input("Please enter your pin...\n")
        if pin == "1234":
            print("Pin accepted")
            return True
        else:
            print("Incorrect pin!")
            attempts += 1
            if attempts >= 3:
                print("We have seized your card for security purposes...\nHave a nice day.")
                return False
            else:
                return pin_func()

    def balance_func():
        nonlocal balance
        withdrawal = input("How much money would you like to withdraw?\n")
        if 0 < int(withdrawal) <= balance:
            return int(withdrawal)
        else:
            print("Insufficient funds!" if int(withdrawal) > balance else "Invalid withdrawal amount!")
            return balance_func()

    def withdraw_func(withdrawal_amount):
        nonlocal balance
        balance -= withdrawal_amount
        print(f"Please take your money and don't forget your card.\nYour remaining balance is {balance}")

    if pin_func():
        amount = balance_func()
        withdraw_func(amount)

cash_machine()
