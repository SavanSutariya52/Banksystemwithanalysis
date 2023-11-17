import pandas as pd
from datetime import datetime
from matplotlib import pyplot as py
from turtle import color
# Function to create a new account
def create_account(accounts_df, account_number, name, balance):
    depositanalisis=pd.read_csv("depositemoney.csv")
    depo=depositanalisis.to_dict('records')
    current_date = datetime.now().strftime('%Y-%m-%d')
    depo.append({'deposite': balance,'Date':current_date,"Ac_Number":account_number})
    depositedata=pd.DataFrame(depo)
    depositedata.to_csv("depositemoney.csv",index=False)
    new_account_data = {"Account Number": account_number, "Name": name, "Balance": balance,"Date":current_date}
    accounts_data = accounts_df.to_dict('records')
    accounts_data.append(new_account_data)
    accounts_df = pd.DataFrame(accounts_data)
    return accounts_df

# Function to deposit money
def deposit(accounts_df, account_number):
    index = accounts_df.index[accounts_df['Account Number'] == account_number].tolist()
    if index:
        amount = float(input("Enter Deposit Amount: "))
        accounts_df.loc[index, 'Balance'] += amount
        depositanalisis = pd.read_csv("depositemoney.csv")
        depo = depositanalisis.to_dict('records')
        current_date = datetime.now().strftime('%Y-%m-%d')
        data1={'deposite': amount, 'Date': current_date,'Ac_Number':account_number}
        depo.append(data1)
        depositedata = pd.DataFrame(depo)
        #print(depositedata)
        depositedata.to_csv("depositemoney.csv",index=False)
        accounts_df.to_csv("bank_accounts.csv")
        print(f"Deposited ${amount}. New balance: ${accounts_df.loc[index, 'Balance'].values[0]}")
    else:
        print("Account not found.")

# Function to withdraw money
def withdraw(accounts_df, account_number):
    index = accounts_df.index[accounts_df['Account Number'] == account_number].tolist()
    if index:
        amount = float(input("Enter Withdrawal Amount: "))
        withdrawanalisis = pd.read_csv("Withdraw.csv")
        depo = withdrawanalisis.to_dict('records')
        current_date = datetime.now().strftime('%Y-%m-%d')
        dict1={'Withdraw':amount,"Ac_Number":account_number,'Date':current_date}
        depo.append(dict1)
        withdraw1=pd.DataFrame(depo)
        if accounts_df.loc[index, 'Balance'].values[0] >= amount:
            accounts_df.loc[index, 'Balance'] -= amount
            withdraw1.to_csv("Withdraw.csv",index=False)
            accounts_df.to_csv("bank_accounts.csv")
            print(f"Withdrew ${amount}. New balance: ${accounts_df.loc[index, 'Balance'].values[0]}")
        else:
            print("Insufficient funds.")
    else:
        print("Account not found.")

# Function to check balance
def check_balance(accounts_df, account_number):
    index = accounts_df.index[accounts_df['Account Number'] == account_number].tolist()
    if index:
        print(f"Balance for Account {account_number}: ${accounts_df.loc[index, 'Balance'].values[0]}")
    else:
        print("Account not found.")

#Analysis
def analysis(accounts_df):
    deposit_df = pd.read_csv("depositemoney.csv")
    while True:
        print("1. Day wise open Account")
        print("2. Day wise deposite Money")
        print("3. Day Wise Withdraw Money")
        print("4. Back to HomePage")
        select1=input("Enter your choice (1-5) ")
        if select1=="1":
            count=list(accounts_df.groupby('Date').size())
            date1=accounts_df['Date'].unique().tolist()
            py.bar(date1,count)
            py.xlabel("Date")
            py.ylabel("Number of Account")
            py.show()
        elif select1=="2":
            count = list(deposit_df.groupby('Date')['deposite'].sum())
            date1 = deposit_df['Date'].unique().tolist()
            py.bar(date1, count)
            py.xlabel("Date")
            py.ylabel("Deposite")
            py.show()
        elif select1=="3":
            withdrawanalisis = pd.read_csv("Withdraw.csv")
            count = list(withdrawanalisis.groupby('Date')['Withdraw'].sum())
            date1 = withdrawanalisis['Date'].unique().tolist()
            py.bar(date1, count)
            py.xlabel("Date")
            py.ylabel("Withdraw")
            py.show()
        elif select1=="4":
            break
        else:
            print("Enter valide range")

# Main function
def main():
    try:
        accounts_df = pd.read_csv("bank_accounts.csv")
        #accounts_df=accounts_df.drop('Unnamed',axis=1)

    except FileNotFoundError:
        columns = ["Account Number", "Name", "Balance"]
        accounts_df = pd.DataFrame(columns=columns)

    while True:
        print("\nBank System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Analysis")
        print("6. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_number = int(input("Enter Account Number: "))
            index = accounts_df.index[accounts_df['Account Number'] == account_number].tolist()
            if index:
                print("Account number allready asign enter new number")
            else:
                name = input("Enter Name: ")
                balance = float(input("Enter Initial Balance: "))
                accounts_df = create_account(accounts_df, account_number, name, balance)
                accounts_df.to_csv("bank_accounts.csv")
                print("Account created successfully.")

        elif choice == "2":
            account_number = int(input("Enter Account Number: "))
            deposit(accounts_df, account_number)

        elif choice == "3":
            account_number = int(input("Enter Account Number: "))
            withdraw(accounts_df, account_number)

        elif choice == "4":
            account_number = int(input("Enter Account Number: "))
            check_balance(accounts_df, account_number)

        elif choice == "5":
            analysis(accounts_df)

        elif choice == "6":
            #accounts_df.to_csv("bank_accounts.csv", index=False)
            print("Exiting. Data saved to 'bank_accounts.csv'")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
