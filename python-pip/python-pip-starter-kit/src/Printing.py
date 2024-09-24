class Printing:
    def arrangePassengerSummary(self,trip_manager):
        sorted_central = dict(sorted(trip_manager.getCentralSummary().items(), key=lambda x: (-x[1], x[0])))
        sorted_airport = dict(sorted(trip_manager.getAirportSummary().items(), key=lambda x: (-x[1], x[0])))
        return(sorted_central,sorted_airport)

    def printSummary(self,trip_manager,collection):
        sorted_central,sorted_airport=self.arrangePassengerSummary(trip_manager)
        
        print(f"TOTAL_COLLECTION  CENTRAL  {collection.getTotalCentral()}  {collection.getDiscountCentral()}")
        print("PASSENGER_TYPE_SUMMARY")
        for i in sorted_central:
            if sorted_central[i] != 0:
                print(i, sorted_central[i])

        print(f"TOTAL_COLLECTION  AIRPORT  {collection.getTotalAirport()}  {collection.getDiscountAirport()}")
        print("PASSENGER_TYPE_SUMMARY")
        for i in sorted_airport:
            if sorted_airport[i] != 0:
                print(i, sorted_airport[i])