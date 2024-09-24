import unittest
from src.Passenger import PassengerFactory
from unittest.mock import patch
from io import StringIO

from src.Fare import Fare
class testFare(unittest.TestCase):
    def setUp(self):
        self.passenger=PassengerFactory().createPassenger(2,150,"ADULT")
        self.price=200
        self.trips=1 
    @patch('sys.stdout', new_callable=StringIO)
    def test_Fare(self,mock_stdout):
        fare=Fare()
        
        total_fare,discount=fare.controlFare(self.passenger,self.price,self.trips)
        print_output = mock_stdout.getvalue()
        print("Captured print output:\n", print_output)
        self.assertEqual(total_fare,201)
        

if __name__=="__main__":
    unittest.main(buffer=False)


        