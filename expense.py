import json
from datetime import datetime
import os

FILE = "daily_expenses.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return {"budget": 0, "logs": {}}

def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=2)

def set_budget():
    amount = float(input("Enter your daily budget: "))
    data = load_data()
    data["budget"] = amount
    save_data(data)
    print("Budget set successfully.\n")

def add_expense():
    data = load_data()
    if data["budget"] == 0:
        print("Please set a daily budget first.\n")
        return

    date = datetime.now().strftime("%Y-%m-%d")
    amount = float(input("Amount spent: "))
    reason = input("Reason: ")

    if date not in data["logs"]:
        data["logs"][date] = []

    data["logs"][date].append({"amount": amount, "reason": reason})
    save_data(data)
    print("Expense added.\n")

def view_today():
    data = load_data()
    date = datetime.now().strftime("%Y-%m-%d")
    today_logs = data["logs"].get(date, [])
    total = sum(item["amount"] for item in today_logs)

    print(f"\nDate: {date}")
    print(f"Budget: Rs.{data['budget']}")
    print("Expenses:")
    for entry in today_logs:
        print(f"- Rs.{entry['amount']} for {entry['reason']}")
    print(f"Total spent: Rs.{total}")
    if total > data["budget"]:
        print("You have exceeded your budget!\n")
    else:
        print("You are within your budget.\n")

def main():
    while True:
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. View Today’s Summary")
        print("4. Exit")

        choice = input("Choose: ")
        if choice == "1":
            set_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_today()
        elif choice == "4":
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()
