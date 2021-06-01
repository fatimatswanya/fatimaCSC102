class FatimaBank:
    loggedinCounter = 0
    def __init__(self, theatmpin, theaccountbalance, thename):
        self.atmpin= theatmpin
        self.accountbalance= theaccountbalance
        self.name= thename
        FatimaBank.loggedinCounter=FatimaBank.loggedinCounter +1

    def CollectMoney(self,amounttowithdraw):
        if(amounttowithdraw > self.accountbalance):
            print('There is no money on gwound')
        else:
            print('Collect your money jare, may you come back sha')

    def ChanePin(self,newPin):
        self.atmpin=newPin
        print('Your pin don change aunty')
    @classmethod               
    def NoofCustomersLoggedin(cls):
