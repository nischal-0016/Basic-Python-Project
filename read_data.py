
def read_data():
    product_data = [["Laptop name","Brand","Price","Quantity","Processor detail","Graphic card"]]
    
    file = open("./database/data.txt","r")
    
    for each in file:
      product_data.append(each.rstrip().split(",")) 

    x = 0
      
    for each in product_data:
        each.insert(0,x) 
        x += 1
    product_data[0][0]="Sn"   
    
    file.close()

    return product_data 
  



   
            
    

      
      
   
   