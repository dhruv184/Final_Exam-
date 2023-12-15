from Product import Product , Store 

store = Store()
def displayMainMenu():

    print("\nPlease select One of the Follwoing Options : \n")

    print("1 to View the list of Products \n")
    print("2 to View Products By Type \n")
    print("3 to Display Total Revenue \n ")
    print("4 to add Product \n")
    print("5 to Exit")

while True :

    displayMainMenu()

    choice = int(input("-->"))

    if choice == 1 :

        print("\nList of Products : \n")

        for p in store.getProducts():

            print(p)

    if choice == 2 :        

        print("\n")
        type= str(input("Enter Product Type (Computer , Phone) : "))
        type.capitalize()
        p = store.findProduct(type)

        if isinstance(p , Product):

            print(p)

    if choice == 4 :

        print("\n")
        code = int(input("Enter Product id : "))
        name = str(input("Enter product Name : "))
        type = str(input("Enter the Type of Product : "))
        price = int(input("Enter product price : "))
        quantity = int(input("Enter product Quantity : "))

        p = Product(code , name , type , price , quantity)

        store.addProduct(p)
        store.saveData()
        
    if choice == 5 :

        print("\n Thanks You \n")
        break    








