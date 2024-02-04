#Nhi Tran

def caffeine():
    caffeine_mg = float(input("mg of caffeine in coffee: "))
    
    caffeine_mg = caffeine_mg / 2
    print("after 6 hours: " + f'{caffeine_mg:.2f}')
    
    caffeine_mg = caffeine_mg / 2
    print("after 12 hours: " +f'{caffeine_mg:.2f}')

    caffeine_mg = caffeine_mg / 4
    print("after 24 hours: " + f'{ caffeine_mg:.2f}')


if __name__ == "__main__":
    caffeine()
