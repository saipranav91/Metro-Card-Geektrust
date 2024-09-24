import unittest
import unittest.main 
from src.Passenger import PassengerFactory
class testPassenger(unittest.TestCase):
    def setUp(self):
        self.passenger=PassengerFactory() 
        self.passenger_type="ADULT"
        self.balance=700 
        self.id=775 
        
    
    def test_Passenger(self):
        adult_passenger=self.passenger.createPassenger(self.id,self.balance,self.passenger_type)
        self.assertEqual(adult_passenger.getId(),self.id)
        self.assertEqual(adult_passenger.getBalance(),self.balance)
        self.assertEqual(adult_passenger.getFare(),200)
        

if __name__=="__main__":
    unittest.main(buffer=False)
    
        
         