class Collection:
    def __init__(self):
        self._total_collection_central = 0
        self._total_collection_airport = 0
        self._discount_central = 0
        self._discount_airport = 0
    def controlCollection(self,passenger,fare,trip_manager,starting_position):
        if starting_position=="CENTRAL":
            self.centralCalculation(passenger,fare,trip_manager)
        elif starting_position=="AIRPORT":
            self.airportCalculation(passenger,fare,trip_manager)
            
    def centralCalculation(self,passenger,fare,trip_manager):
        price=passenger.getFare()
        trips=trip_manager.getTrips(passenger.getId())
        
        total_fare,discount=fare.controlFare(passenger,price,trips)
        self._total_collection_central=self._total_collection_central+total_fare
        self._discount_central=self._discount_central+discount
    def airportCalculation(self,passenger,fare,trip_manager):
        price=passenger.getFare()
        trips=trip_manager.getTrips(passenger.getId())
        total_fare,discount=fare.controlFare(passenger,price,trips)
    
        self._total_collection_airport=self._total_collection_airport+total_fare
        self._discount_airport=self._discount_airport+discount
    
    def getTotalCentral(self):
        return self._total_collection_central 
    def getTotalAirport(self):
        return self._total_collection_airport 
    def getDiscountCentral(self):
        return self._discount_central
    def getDiscountAirport(self):
        return self._discount_airport 
    