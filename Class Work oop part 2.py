class oranges:
    price=50
    stockquantity=100    
    def __init__ (self, amount):
        self.amount = amount 

    def CustomerOrder(self):
        if self.amount > oranges.stockquantity:
            print('Unfortunately We do not have enough oranges. Reduce your order please.')
        else:
           print(f'Thank you for placing an order.Your bill is {oranges.price * self.amount}')    


customer_1= oranges(int(input("Enter:")))
customer_1.CustomerOrder()


