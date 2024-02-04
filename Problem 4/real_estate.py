#Nhi Tran

def real_estate():
    
    current_price = int(input("What is the current price of the house? "))
    last_month_price = int(input("What was last month's price of the house? "))
    
    price_change = last_month_price - current_price
    mortgage = (current_price * 0.051) / 12

    print("This house is $" + f'{last_month_price:.2f}' + ". The change is $" + f'{price_change:.2f}' ". The estimated monthly mortage is $" + f'{mortgage:.2f}' +".")


if __name__ == "__main__":
    real_estate()
