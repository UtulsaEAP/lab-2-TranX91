#Nhi Tran

def right_arrow():
    base_char = input()
    head_char = input()

    

    row1 = 6 *''+ head_char
    row2 = 6* base_char + 2* head_char
    row3 = row2 + head_char
    
    
    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()
