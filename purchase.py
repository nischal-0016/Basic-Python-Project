from clean import clear_screen
from display import display
from read_data import read_data
import datetime

N = []

def purchase():
    while True:    
        manufacturers_name = input('Enter Manufacturers Name: ')
        if manufacturers_name == '':
            print('Enter Manufacturers Name and Try again.')
        else:
            break

    clear_screen()
    display

    K = read_data()
    purchase = True

    while purchase: 
              
        try:
            display()  
            print("How many quantity would you like to add?")
            X = int(input('Enter the SN from above table to add the quantity: '))
            Qty = int(input(f'How many {K[X][1]} do you want to add to quantity?: '))
            rate = int(K[X][3].strip().strip("$"))
            name = K[X][1]
            brand = K[X][2]
            total_Price = (rate*Qty)

            if Qty == 0:
                print("Quantity must be greater than 0,TRY AGAIN!.")
            else:
                print(f'{name} Quantity Added.')

                N.append([name, brand, total_Price])

                file=open("Quantity Added"+ manufacturers_name+".txt","w")
                file.write("manufacturers name:"+manufacturers_name)
                file.write(f"\ndate & time: {datetime.datetime.now()}\n")
                file.write('------------------------------------------\n')
                file.close()
                

                K[X][4] = str(int(K[X][4])+Qty)

                file=open("data.txt", "w")
                for i in range(1, len(K)):
                    each = K[i]
                    file.write(f'{each[1]},{each[2]},{each[3]},{each[4]},{each[5]},{each[6]}\n')
                file.close()

                while True:
                    user_input=input(f'Would you like to add more quantity? (Y/N): ').upper()

                    if user_input== "Y":
                        clear_screen()
                        break

                    elif user_input== 'N':
                        clear_screen()
                        purchase=False
                        for s in N:
                            file = open("purchased"+ manufacturers_name+".txt", "a+")
                            file.write(f'Laptop Name: {s[0]}\n')
                            file.write(f'Brand: {s[1]}\n')
                            file.write(f'Net amount: {s[2]}\n')
                            file.write('------------------------------------------\n')
                            file.close()

                        amount=total_Price
                        vat_amount=amount * 0.13
                        total_amount=amount + vat_amount
                        file=open('purchased"+ manufacturers_name+".txt", "a+')
                        file.write(f'Total amount without VAT: {total_Price}\n')
                        file.write(f'VAT amount (13%): {vat_amount}\n')
                        file.write(f'Total amount including VAT: {total_amount}\n')
                        file.close()
                        break

                    else:
                        print('Please enter Y or N only.')

        except Exception as e:
            print(e)


