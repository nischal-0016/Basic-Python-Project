from read_data import read_data

def display():

    file_data = read_data()
    print('------------------------------------------------------------------------------------------------------------------------------------')
    for row in file_data:
        print(row[0].ljust(5) + '|', end='')
        for each in row[1:]:
            print(each.ljust(20) + '|', end='')
        print()
        print('------------------------------------------------------------------------------------------------------------------------------------')




