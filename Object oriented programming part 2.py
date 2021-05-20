class Coffee:
    coffeecupcounter =0  
    def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk = themilk
        self.sugar = thesugar
        self.coffeemate = thecoffeemate
        Coffee.coffeecupcounter=Coffee.coffeecupcounter+1
        print(f'You now have your coffee with {self.milk} milk, {self.sugar} sugar, {self.coffeemate} coffeemate')

mysugarfreecoffee= Coffee(2,0,1)
print(mysugarfreecoffee.sugar)
mysweetcoffee =Coffee(2,100,1)
print(mysweetcoffee.sugar)
print(f'We have made {Coffee.coffeecupcounter} coffee cups so far!')
print(f'We have made {mysugarfreecoffee.coffeecupcounter} coffee cups so far!')
print(f'We have made {mysweetcoffee.milk} coffee cups so far!')
print(f'We have made {mysweetcoffee.coffeecupcounter} coffee cups so far!')