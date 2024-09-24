import unittest
from unittest.mock import patch
from io import StringIO
from src.TripManager import TripManager
from src.Fare import Fare
from src.Passenger import PassengerFactory
from src.Collection import Collection

class TestCollections(unittest.TestCase):
    
    def setUp(self):
        # Initialize objects needed for the test
        self.trip_manager = TripManager()
        self.fare = Fare()
        self.passenger_factory = PassengerFactory()
        self.collection = Collection()
        self.starting_position = "AIRPORT"
        self.id = 1
        self.balance = 345
        self.passenger_type = "ADULT"
        
        # Create a passenger and set up the passenger registry
        self.passenger = self.passenger_factory.createPassenger(self.id, self.balance, self.passenger_type)
        self.trip_manager.addRegistry(self.id,self.passenger) 
    
    @patch('sys.stdout', new_callable=StringIO)  
    def test_collection_central(self, mock_stdout):
        # Call the method you want to test
        self.collection.controlCollection(self.passenger, self.fare, self.trip_manager, self.starting_position)
        
        # Capture the print output from the Collection module
        print_output = mock_stdout.getvalue()
        
        # Print the captured output for debugging purposes
        print("Captured output from Collection:\n", print_output)
        
        # Check the expected outcome
        self.assertEqual(self.collection.getTotalAirport(), 200)

if __name__ == "__main__":
    unittest.main(buffer=False)
