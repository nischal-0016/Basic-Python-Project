from clean import clear_screen
from display import display
from read_data import read_data
import datetime

N = []

def sell():
    while True:    
        customer_name = input("Enter Customer Name: ")
        if customer_name == '':
            print("Please Enter Customer Name and Try again.")
        else:
            break

    clear_screen()
    display

    J = read_data()
    sell = True

    while sell:   
        try:
            display()
            print("Enter" " " +customer_name+ " "" choice Laptop")
            X = int(input("Enter SN number: "))
            Qty = int(input(f"How many {J[X][1]} does"" "+customer_name+" "" want to buy?: "))
            rate = int(J[X][3].strip().strip("$"))
            name = J[X][1]
            brand = J[X][2]
            total_Price = (rate*Qty)

            if float(J[X][4]) < Qty:
                print(f"Sorry,{name} is out of stock.")
                
            elif Qty == 0:
                print("Quantity must be greater than 0,Try again.")

            else:
                print(f"{name} Sold.")

                N.append([name, brand, total_Price])

                file = open("Sell"+ customer_name+".txt","w")
                file.write("Customer name:"+customer_name)
                file.write(f"\ndate & time: {datetime.datetime.now()}\n")
                file.write('------------------------------------------\n')
                file.close()
                    

                J[X][4] = str(int(J[X][4])-Qty)

                file = open("data.txt", "w")
                for i in range(1, len(J)):
                    each = J[i]
                    file.write(f"{each[1]},{each[2]},{each[3]},{each[4]},{each[5]},{each[6]}\n")
                file.close()

                while True:
                    user_input = input(f"Does"" "+customer_name+" "" wants to buy anything else? (Y/N): ").upper()

                    if user_input == "Y":
                            clear_screen()
                            break

                    elif user_input == "N":
                        clear_screen()
                        sell = False
                        Shipping_cost = float(input(f'Please enter Shipping_cost: '))
                        for s in N:
                            file = open("sell"+ customer_name+".txt","a+")
                            file.write(f'Laptop Name: {s[0]}\n')
                            file.write(f'Brand: {s[1]}\n')
                            file.write(f'Net amount: {s[2]}\n')
                            file.write('------------------------------------------\n')
                            file.close()

                        total = sum(int(_[2]) + Shipping_cost for _ in N)
                        file = open("sell"+ customer_name+".txt","a+")
                        file.write(f"\n Shipping cost: {Shipping_cost}\n Total cost: {total}")
                        break

                    else:
                        print("Please enter Y or N only.")
            
        except Exception as e:
            print(e)




