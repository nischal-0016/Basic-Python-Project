# import in-built modules os and datetime
import os
import datetime

# creating function that take details to create selling invoice
def create_selling_invoice(name_oflaptop,laptop_brand,price,quantity,shopper):
    
    # creating date object to get the date
    date_time = datetime.datetime.now()
    purchase_date = date_time.strftime("%x")
    purchase_time = date_time.strftime("%X")
    shipping_amt =(15/100 * price) 
    total_amt_without_shipping = str(price * quantity)
    grand_total = str((price * quantity) + shipping_amt)
    record = "./invoices/selling invoices/" + shopper + "_sold.txt"

#  to check if the file name already exists
    if os.path.exists(record):
        # initializing counter
        i = 1

        # using loop to check if the file name exists and increase the counter to create new file name
        while True:
            new_record = f"{os.path.splitext(record)[0]}_{i}_{os.path.splitext(record)[1]}"
            if not os.path.exists(new_record):
                record = new_record
                break
            i+=1
# creating a new file with given file name
    f = open(record,"w") 
    f.write("----------------------------------------------\n")
    f.write("||            CUSTOMER RECEIPT              ||\n")
    f.write("----------------------------------------------\n")
    f.writelines(["||   Laptop name: " + name_oflaptop.ljust(26) ,"||""\n"
                     "||   Brand name: " + laptop_brand.ljust(27),"||""\n"
                     "||   Customer name: " + shopper.ljust(24),"||""\n"
                     "||   Date of purchase: " + purchase_date.ljust(21),"||""\n"
                     "||   Time of purchase: " + purchase_time.ljust(21),"||""\n"
                     "||   Shipping amount: " + "$"+str(shipping_amt).ljust(21),"||""\n"
                     "||   Total amount without shipping: " + "$"+total_amt_without_shipping.ljust(7),"||""\n"
                     ])
    f.write("----------------------------------------------""\n")
    f.writelines(["||   Grand total: " + "$"+grand_total.ljust(25),"||"])
    f.write('\n')
    f.write("----------------------------------------------")
    f.close()

# opening and reading the invoice to print in the shell
    invoiceFile = open(record,'r')

    for each in invoiceFile:
        print(each)
    invoiceFile.close()
    # closing the opened file
    



# creating function that take details to create ordering invoice
def create_ordering_invoice(company_name,company_add,contact,name_oflaptop,laptop_brand,price,quantity):
   
    # creating date object to get the date
    date_time = datetime.datetime.now()
    order_date = date_time.strftime("%x")
    order_time = date_time.strftime("%X")
    vat_amt = (13/100 * price)
    net_amt = str(price * quantity)
    grand_total = str((price*quantity) + vat_amt)
    record = "./invoices/ordering invoices/" + company_name + ".txt"

#  to check if the file name already exists
    if os.path.exists(record):
        # initializing counter
        i = 1

# using loop to check if the file name exists and increase the counter to create new file name
        while True:
            new_record = f"{os.path.splitext(record)[0]}_{i}_{os.path.splitext(record)[1]}"
            if not os.path.exists(new_record):
                record = new_record
                break
            i+=1
# creating a new file with given file name
    f = open(record,"w") 
    f.write("----------------------------------------------\n")
    f.write("||             COMPANY RECEIPT              ||\n")
    f.write("----------------------------------------------\n")
    f.writelines(["||   Company name: " + company_name.ljust(25) ,"||""\n"
                      "||   Company address: " + company_add.ljust(22),"||""\n"
                      "||   Company contact: " + str(contact).ljust(22),"||""\n"
                      "||   Laptop name: " + name_oflaptop .ljust(26) ,"||""\n"
                      "||   Brand name: " + laptop_brand.ljust(27),"||""\n"
                      "||   Date of order: " + order_date.ljust(24),"||""\n"
                      "||   Time of purchase: " + order_time.ljust(21),"||""\n"
                      "||   Net amount: " + "$"+ net_amt.ljust(26),"||""\n"
                      "||   VAT amount: " + "$"+ str(vat_amt).ljust(26),"||""\n"
                      ]) 
    f.write("----------------------------------------------""\n")
    f.writelines(["||   Grand Total: " + "$"+ grand_total.ljust(25),"||"])                
    f.write("\n")
    f.write("----------------------------------------------")
    f.close()

# opening and reading the invoice to print it in the shell
    invoiceFile = open(record,'r') 

    for each in invoiceFile:
        print(each)

    invoiceFile.close()
    # closing the opened file



