items = []

class Cart:
    def __init__(self):
        self.items = items

    def showAll(self):
        print(self.items)

    def addItem(self, items):
        self.items.append(items)
        return self

    def removeItem(self, id):
        for i, d in enumerate(items):
            if d['id'] == id:
                return items.pop(i)

    # def totalItems()

cart = Cart()

# Do some chainings
(
cart.addItem({ 'item_id': 1, 'price': 30000, 'quantity': 3 })     # By default quantity is 1
    .addItem({ 'item_id': 3, 'price': 5000, 'quantity': 2 })
    .addItem({ 'item_id': 4, 'price': 400, 'quantity': 6 })
)

# cart.totalItems() # 3

# cart.totalQuantity() # 11

# cart.totalPrice() # 51200

cart.showAll() # Show all items in cart

# cart.checkout() # Store data in a file i.e : cart.txt