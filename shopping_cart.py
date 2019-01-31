# loop and continue to ask until user quits, have the ability to perform all three functions:
# def shoppingCart(): (def addItem(item):  def removeItem(item):  def showCart():) shoppingCart() pass

itemStored = []

def addItem(): #def addItem(item):
    added_item = input("What would you like to get?: ")
    itemStored.append(added_item)
def removeItem(): #def removeItem(item)
    removed_item = input("Which item would you like to remove? ")
    if removed_item in itemStored:
        itemStored.remove(removed_item)
    else:
         print("The item does not exist in the item you chose.")
    #TODO: Show the current list. If there in nothing in the list, ask to add some items.
def showCart():
    for items in itemStored:
        print(items)
    #TODO: Add if statement to tell that there is no item if there is no item in the list.
    #TODO: Add something like "Here's your list: ",


def shoppingCart():
    print("Would you like to add items to the cart, remove items from the cart, show the current items you chose?")
    while True:
        select = input("Please select an option from 'add', 'remove' or 'show'. If you would like to quit, please type 'quit'.")

        if select.lower() == "quit":
            for items in itemStored:
                print("Here's your list: ", items)
            break
            #TODO: Add if statement to see if they want to go back to the choice again.

        elif select.lower() == "add":
            addItem()
        elif select.lower() == "remove":
            removeItem()
        elif select.lower() == "show":
            showCart()
        else:
            print("I didn't understand. Could you type again?")

try:
    shoppingCart()
except:
    print("no, wrong")
