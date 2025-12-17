# Daily Expense Tracker Program

# Aa program user ni daily expenses store ane analyze kare che
# Python Basics + File Handling use kari ne banavyu che


# Expenses add karva mate function

def add_expense():
    # user pase thi date levani
    date = input("Enter Date (DD-MM-YYYY) : ")

    # category leva ane uppercase ma convert karva 
    # etle food / Food / FOOD badhu same count thase
    category = input("Enter Category (Food, Travel, etc) : ").upper()

    # Amount valid che ki nai ee check karva mate
    try:
        amount = float(input("Enter Amount : "))
    except ValueError:
        print("Please Enter a Valid Number")
        return
    

     # Expense no note
    note = input("Enter Note : ")
    
    # File open kari ne data append mode ma save karvanu
    with open("expenses.txt", "a") as file:
        file.write(f"{date}, {category}, {amount}, {note} \n")
    print("Expense Successfully Added \n")


# badha expenses dekhadva mate

def view_expenses():
    print("\n--- All Expenses ---")

    try:
        # File read mode ma open karvu
        with open("expenses.txt", "r") as file:
            for line in file:
                # Line ne comma thi split karvi
                date, category, amount, note = line.strip().split(",")
                # Expense ne proper format ma print karvu
                print(f"Date: {date} | Category: {category} | Amount: {amount} | Note: {note}")
    except FileNotFoundError:
        print("No expenses found. \n")


# Total Expenses means badha amount no sum

def total_expense():
    # Total expense store karva mate variable
    total = 0

    try:
        # expenses.txt file read mode ma open karvi 
        with open("expenses.txt", "r") as file:
            # File ni ek ek line read karvi
            for line in file:
                # line ne comma thi todvu
                parts = line.strip().split(",")
                # parts[2] amount hoy che
                # ene float ma convert kari ne total ma add karvu
                total += float(parts[2])
        # final total print karvu
        print(f"\n Total Expenses: {total}\n")
    except FileNotFoundError:
        # jo file j naa hoy toh
        print("No Expense is Recorded \n")
 

# Category Wise means category pramane total

def category_wise_summary():
    # category wise total store karva mate empty dictonary
    summary = {}

    try:
        # file read mode ma open karvi
        with open("expenses.txt", "r") as file:
            # file ni badhi lines read karvi
            for line in file:
                # line ne comma thi split karvi
                date, category, amount, note = line.strip().split(",")
                # amount ne float ma convert karvu
                amount = float(amount)
                # jo category already dictonary ma che
                if category in summary:
                    summary[category] += amount
                else:
                    # nai hoy toh navi category add karvi
                    summary[category] = amount
        # category wise summary print karvi
        print("\n---- Category Wise Summary ----")
        for category in summary:
            print(f"{category}: {summary[category]}")
    except FileNotFoundError:
        # jo file j na hoy toh
        print("No Expense is Recorded")



# Main Menu Function

def menu():
    while True:
        print("\n===== Daily Expense Tracker ======")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your Choice : ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_wise_summary()
        elif choice == "5":
            print("Exiting Program")
            break
        else:
            print("Invalid Choice")


# program start thava mate menu call karvu
menu()