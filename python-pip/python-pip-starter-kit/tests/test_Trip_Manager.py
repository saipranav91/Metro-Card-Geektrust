import unittest 
from src.TripManager import TripManager


class testTripManager(unittest.TestCase):
    def setUp(self):
        
        self.starting_position="CENTRAL"
        self.passenger_type="ADULT"
        self.trip_manager=TripManager()
    
    def test_Trip_Manager(self):
        self.trip_manager.updateSummary(self.starting_position,self.passenger_type)
        self.assertEqual(self.trip_manager.getCentralSummary()[self.passenger_type],1)
        
        

if __name__=="__main__":
    unittest.main(buffer=False)
        
        