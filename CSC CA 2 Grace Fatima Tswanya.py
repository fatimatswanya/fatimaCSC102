class OnlineStore:
    DiscountPrice=100000   
    def __init__(self, NumberofItemsBought, TotalCost):
        self.NumberofItemsBought=NumberofItemsBought
        self.TotalCost=TotalCost

    def DiscountCalculator(self):

        if (self.NumberofItemsBought <10)>OnlineStore.DiscountPrice:
            print('You are eligible for a 10 percent discount, your total is {self.Total.Cost*0.1}')
        elif(self.NumberofItemsBought>10)>OnlineStore.DiscountPrice:
            print(str('You have earned a giftcard and a 10 percent discount, your total is {self.Total.Cost*0.1} '))
        else:
            pass    


customer1=OnlineStore(int(input('Enter Number Of Items Bought:')),int(input('Enter Total Cost:')))
customer1.DiscountCalculator() 
