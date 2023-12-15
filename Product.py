import csv

class Product : 

    def __init__(self , code , name , type , price , quantity ):

        self.code = code
        self.name = name
        self.type = type
        self.price = price
        self.quantity = quantity  

    def __str__(self):

        return f"\nCode : {self.code} , Name : {self.name} , Type : {self.type} , Price : {self.price} , Quantity : {self.quantity}"


class Data : 

    @staticmethod  

    def getData(filename):

        products = [ ]

        with open(filename , "r") as file :

            reader = csv.reader(file)

            for row in reader:

                p = Product(row[0] , row[1] , row[2] , row[3] , row[4])
                products.append(p)

            return products

    @staticmethod

    def writeData(filename , rows):

        with open(filename , 'w' , newline ='') as file:

            writer = csv.writer(file)  

            writer.writerows(rows)

class Store:

    def __init__(self):

        self.products = Data.getData('products_sales.csv')

    def addProduct(self , product):

        self.products.append(product)

    def getProducts(self):

        return self.products
        
    def saveData(self):

        rows = [ ]

        for p in self.products:

            row = [p.code , p.name , p.type , p.price , p.quantity]
            rows.append(row)

        Data.writeData('products_sales.csv' , rows)   

    def findProduct(self, type):

        p = None 

        for product in self.products:

            if product.type == type :
               
                p = product
                print(p)
    
    