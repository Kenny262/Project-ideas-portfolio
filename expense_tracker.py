def main():
    print("Welcome to your personal budget Tracker!")
    budget = get_user_budget()
    # User enters monthly pay
    expenses = get_user_expenses()
    #user enters expenses so info can be out into file
    save_exp_budget_to_file(budget, expenses)
    #save all enterd info into a file
    summarize_monthly_budget(budget, expenses)
    #show daily spending avg and what range you are within monthly budget and give simple advice
    #breaks down the amount spent in each category by percent 

def get_user_budget():
    return float(input("What is your monthly take-home pay?: $"))
    
def get_user_expenses():
    categories = ["Housing", "Groceries", "Transportation", "Misc", "Healthcare", "Dining Out", "Education", "Savings"]
    expenses = {}
    
    while True:
        print("Select a Category:")
        for i, category_name in enumerate(categories):
            print(f"{i + 1}. {category_name}")

        selected_index = input("Enter a category number (or 'done' to finish): ")
        if selected_index.lower() == "done":
            break
        
        try:
            selected_index = int(selected_index)
            if 1 <= selected_index <= len(categories):
                category = categories[selected_index - 1]
                expenses[category] = float(input(f"Enter the amount for '{category}': $"))
            else:
                print("Invalid category number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid category number or 'done' to finish.")
    
    return expenses

def save_exp_budget_to_file(budget, expenses):
    with open("expense_budget.txt", "w") as file:
        file.write(f"Monthly Budget: {budget}\n")
        file.write("Expenses:\n")
        for category, amount in expenses.items():
            file.write(f"{category}: {amount}\n")

def summarize_monthly_budget(budget, expenses):
    total_expenses = sum(expenses.values())
    remaining_budget = budget - total_expenses
    percentage_spent = (total_expenses / budget) * 100
    expense_breakdown = ()
    
    print("\n--- Monthly Budget Summary ---")
    print("Total Expenses: $", total_expenses)
    print("Remaining Budget: $", remaining_budget)
    print("Percentage Spent: ", percentage_spent, "%")


    if percentage_spent >= 100:
        print("You have exceeded your budget! Consider major financial changes.")
    elif percentage_spent >= 75:
        print("You have reached 80% of your budget. Consider cutting down on expenses.")
    elif percentage_spent >= 50:
        print("You have reached 50% of your budget.")
    else:
        print("You are within your budget.")

    print("Average Daily Spending: $", total_expenses / 30)  # Assuming 30 days in a month

    print("\n".join([f"{category}: {amount}  ({(amount / budget * 100):.2f}%)"
                    for category, amount in expenses.items()]))

if __name__ == "__main__":
    main()

