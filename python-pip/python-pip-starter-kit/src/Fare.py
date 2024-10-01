import math 
class Fare:
    def controlFare(self,passenger,price,trips):
        discount=0
        if trips%2==0:
            price=price//2 
            discount=discount+price
        total_fare=self.fareCalculation(passenger,price)
        return (total_fare,discount)
        
        
    @staticmethod   
    def serviceTax(self,insufficient):
        tax=0.02
        return math.ceil(tax*insufficient)
        
    def fareCalculation(self,passenger,price):
        currentBalance=passenger.getBalance()
        if currentBalance>=price:
            passenger.adjustBalance(price)
            return price
        else:
            insufficient=price-currentBalance
            passenger.adjustBalance(price)
            service_tax=self.serviceTax(insufficient)
            return price+service_tax