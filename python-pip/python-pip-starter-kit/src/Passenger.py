from abc import ABC,abstractmethod

class Passenger(ABC):
    def __init__(self,id,balance):
        self._id=id 
        self._balance=balance
        self._fare=0
    @abstractmethod
    def getFare(self):
        pass 
    def getId(self):
        return self._id 
    def getBalance(self):
        return self._balance 
    def adjustBalance(self,amount):
        if self._balance>=amount:
            self._balance=self._balance-amount 
        else:
            self._balance=0

class AdultPassenger(Passenger):
    def __init__(self,id,balance):
        super().__init__(id,balance)
        self._fare=200
    
    def getFare(self):
        return self._fare 

class KidPassenger(Passenger):
    def __init__(self,id,balance):
        super().__init__(id,balance)
        self._fare=50
    
    def getFare(self):
        return self._fare 
    
class SeniorCitizen(Passenger):
    def __init__(self,id,balance):
        super().__init__(id,balance)
        self._fare=100
    
    def getFare(self):
        return self._fare 

# class PassengerFactory:
#     def createPassenger(self,id,balance,passenger_type):
#         if passenger_type=="ADULT":
#             return AdultPassenger(id,balance)
#         elif passenger_type=="KID":
#             return KidPassenger(id,balance)
#         elif passenger_type=="SENIOR_CITIZEN":
#             return SeniorCitizen(id,balance)
#         else:
#             raise Exception(f"{passenger_type} not found")

#  the Open/Closed Principle (OCP), as every time a new passenger type is added, you'll need to modify the createPassenger method, making it harder to maintain and extend.

# Using a more flexible approach like registering passenger types dynamically

class PassengerFactory:
    def __init__(self):
        self._passenger_types = {#storing in dict makes it more flexible for adding other types
            "ADULT": AdultPassenger,
            "KID": KidPassenger,
            "SENIOR_CITIZEN": SeniorCitizen,
        }
    def addPassengerTypes(self,key,value):
        self._passenger_types[key]=value
        
    
    def createPassenger(self,id,balance,passenger_type):
        if passenger_type in self._passenger_types:
            return self._passenger_types[passenger_type](id,balance)
        else:
            raise Exception(f"{passenger_type} not found")
        
#HERE it is more flexible here if i want to add another age specific passenger all i have to do is create a instance 
#of Passenger and create new class and just add that to the passenger_types dict it follows Open/close principle and better than previous one

        