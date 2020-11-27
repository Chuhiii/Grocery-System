def FirstCategory():
    print("Select a Category:")
    print("[1] Beverages")
    print("[2] Dry Goods")
    print("[3] Frozen Goods")
    print("[4] Meat")
    print("[5] Process Food")

    ans = int(input("\nEnter the name of category: "))

    catego = Category(ans)

    if  cate == 1:
        print("\nCoke")
        print("Mountaindew")
        print("Pepsi")
        print("Royal\n")
    elif cate == 2:
        print("\nFlour")
        print("sugar")
        print("coffee mate\n")
    elif cate == 3:
        print("\nChicken")
        print("Pork")
        print("Beef\n")
    elif cate == 4:
        print("\nHam")
        print("Binabad")
        print("Tocino\n")
    elif cate == 5:
        print("\nVienna sausage")
        print("Hotdog\n")
    else:
        print("\nIncorrect option")

#Declaration of Variables   
items = []
  
#Shopper Dictionary this will use to get the informaton of the shopper.     
shopper = {
    "Name: ": name,
    "Address: ": address,
    "Contact No.: ": contact
}
#MAIN MEthod
print("************************************************")
print("*                 Once's Mart                  *")
print("************************************************\n")
print("[1] Shop")
print("[2] Cart list")
print("[3] Exit")

firstQ = int(input("Input the command: "))

#Input item in to the list
itemShopper = input("Enter products you want to add to cart: ")
itemQuantity = input("Quantity: ")
items.append(itemShopper)
items.append(itemQuantity)

#Shopper main method
name = input("Name: ")
address = input("Address: ")
contact = input("Contact ")

print(shopper)

  