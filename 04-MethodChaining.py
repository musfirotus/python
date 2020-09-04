import json

items = []

class Cart:
    def __init__(self):
        self.items = items

    def showAll(self):
        print(self.items)

    def addItem(self, items):
        self.items.append(items)
        return self

    def removeItem(self,value):
        for i, val in enumerate(self.items):
            if val['item_id'] == value['item_id']:
                del self.items[i]
        return self

    def totalItems(self):
        count = len(self.items)
        print(f"Total items: {count}")

    def totalQuantity(self):
        sumQuantity = sum(item['quantity'] for item in items)
        print(f"Total Quantity: {sumQuantity}")

    def totalPrice(self):
        sumPrice = sum(item['price'] for item in items)
        print(f"Total Price: {sumPrice}")

    def checkout(self):
        f = open("cart.txt", "a+")
        f.write(json.dumps(self.items))
        f.close()
        print("Sukses Checkout!")

cart = Cart()

# Do some chainings
(
cart.addItem({ 'item_id': 1, 'price': 30000, 'quantity': 3 })     # By default quantity is 1
    # .addItem({ 'item_id': 2, 'price': 10000 })
    .addItem({ 'item_id': 3, 'price': 5000, 'quantity': 2 })
    .removeItem({'item_id': 3})
    .addItem({ 'item_id': 4, 'price': 400, 'quantity': 6 })
    # .addDiscount('50%')
)

cart.totalItems() # 3

cart.totalQuantity() # 11

# bisa menjadi 35400 karena ada item yang saya tambahkan
# bisa juga menjadi 30400 karena removeItem dianggil duluan
cart.totalPrice() # 51200

cart.showAll() # Show all items in cart

cart.checkout() # Store data in a file i.e : cart.txt