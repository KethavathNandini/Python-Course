balance = 0
kyc_document={}

def check_balance():
    print(f"your current balance is: {balance} ")
    print("======================")


def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("cannot deposit a negative or zero amount")
        print("======================")


def withdraw(amount):
    global balance
    if amount <= 0:
        print("cannot withdraw a negative or zero amount")
    elif amount > balance:
        print("Cannot withdraw. Insufficient balance.")
    else:
        balance -= amount

def update_kyc(docs):
    global kyc_document
    kyc_document.update(docs)

def check_kyc():
    global kyc_document
    if len(kyc_document) == 0:
        print("KYC not done")
    else:
        for docs in kyc_document:
            print(f"{docs}: {kyc_document[docs]}")


if __name__ =="__main__":
    while True:
        print("Welcome to SMILE bank")
        print("======================")
        print("1. Check your balance")
        print("2. Deposit an amount")
        print("3. Check Kyc")
        print("4. Update kyc")
        print("5. Withdraw an amount")
        print("6. Quit")
        print("======================")

        choice = input("Enter your choice(1-6): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amt = float(input("Enter the amount to deposit: "))
            deposit(amt)
            print(f"Amount {amt} deposited successfully")
        elif choice =='3':
            check_kyc()
        elif choice == '4':
            kyc_docs = {}
            documents =int(input("Enter the number of documents you wnt to add:"))
            for i in range(documents):
                key =input("Enter the document type: ")
                value = input("Enter the document number")
                kyc_docs[key] = value
            update_kyc(kyc_docs)
            print("kyc updated!")
        elif choice == '5':
            amt = float(input("Enter the amount to withdraw: "))
            withdraw(amt)
            print(f"Amount{amt} withdrawn successfully")

        elif choice == '6':
            print("Quiting, have a nice day☺️")
            break
        else:
            print("Invalid choice!! Re-try.")


print("Thank you for banking with us!")