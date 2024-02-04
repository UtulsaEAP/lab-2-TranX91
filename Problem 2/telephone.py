#Nhi Tran

def telephone():
    phone_number = int(input("Enter a phone number:" ))

    line_number = phone_number % 10000
    line_number =  "-" + str(line_number)
    phone_number = phone_number // 10000

    prefix = phone_number % 1000
    prefix = " " + str(prefix)
    phone_number = phone_number // 1000
    
    area_code = "(" + str(phone_number) + ")"

    final = area_code + prefix + line_number 
    print(final)
if __name__ == "__main__":
    telephone()
