#Global Variables
federal_Tax = 0.10
state_Tax = 0.05
social_Security = 0.062
TRANSACTIONS = []


# TO-DO Calculate gross pay
def calculate_gross_pay(wage, hours):
    gross_pay = wage * hours
    return gross_pay

# TO-DO Calculate withholding
def calculate_withholding(gross_pay):

    federal = gross_pay * federal_Tax
    state = gross_pay * state_Tax
    social = gross_pay * social_Security  
    return federal, state, social

# TO-DO Calculate net pay
def calculate_net_pay():

    wage = float(input("Enter your hourly wage: "))
    hours = float(input("Enter hours worked: "))

    gross_pay = calculate_gross_pay(wage, hours)

    federal, state, social = calculate_withholding(gross_pay)

    net_pay = gross_pay - federal - state - social

    print("\n--------PAY REPORT--------")
    print(f"Gross Pay:          ${gross_pay:.2f}")
    print(f"Federal Tax:        ${federal:.2f}")
    print(f"State Tax:          ${state:.2f}")
    print(f"Social Security:    ${social:.2f}")
    print("----------------------------")
    print(f"Net Pay:            ${net_pay:.2f}")

# TO-DO Create your menu and program

    # Track income and expenses
def track_transactions():

    while True:

        transaction = input("Enter transaction name: ")
        amount = float(input("Enter amount (use negative sign for expenses): "))

        TRANSACTIONS.append(amount)

        another = input("Another? (Y/N): ").upper()

        if another != "Y":
            break

    # Discretionary Report
def discritionary_report():

    total_income = 0
    total_expenses = 0

    for amount in TRANSACTIONS:
        if amount >= 0:
            total_income += amount
        else:
            total_expenses += amount

    discretionaries = total_income + total_expenses

    print("\n--------MONTHLY SUMMARY--------")
    print(f"Total Income:   Ghc{total_income:.2f}")
    print(f"Total Expenses: Ghc{abs(total_expenses):.2f}")
    print("---------------------------------")
    print(f"Discretionary:  Ghc{discretionaries:.2f}")

    # Program Menu
def display_menu():

    print("\n======OWOAHENE FINANCE TRACKER======\nPowered by K.Ache Ops. All Right Reserved")
    print("\n.....Start Here.....")
    print("1. Calculate Net Pay")
    print("2. Track Revenue and Expenses")
    print("3. Report Monthly Discretionaries")
    print("4. Exit")


def main():

    choice = ""
    while choice !="4":
        display_menu()
        choice = input("Enter your choice: ")
        if choice =="1":
            calculate_net_pay()

        elif choice =="2":
            track_transactions()

        elif choice =="3":
            discritionary_report()

        elif choice =="4":
            print("...Thank you for using Owoahene Finance Tracker...!")

        else:
            print("Invalid choice. Please try again")

# Start Program
main()



