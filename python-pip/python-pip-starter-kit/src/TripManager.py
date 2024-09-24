class TripManager:
    def __init__(self):
        self._passenger_registry={}
        self._passenger_summary={
            "CENTRAL":{"ADULT": 0, "KID": 0, "SENIOR_CITIZEN": 0},
            "AIRPORT":{"ADULT": 0, "KID": 0, "SENIOR_CITIZEN": 0}
        }
        
    def updateSummary(self,starting_postiton,passenger_type):
        self._passenger_summary[starting_postiton][passenger_type]=self._passenger_summary[starting_postiton][passenger_type]+1
    def getCentralSummary(self):
        return self._passenger_summary["CENTRAL"]
    def getAirportSummary(self):
        return self._passenger_summary["AIRPORT"] 
    
        
    
    def updateTrips(self,id):
        self._passenger_registry[id]["trips"]=self._passenger_registry[id]["trips"]+1
    def addRegistry(self,id,passenger):
        self._passenger_registry[id]={"passenger":passenger,"trips":1}
    def getPassenger(self,id):
        return self._passenger_registry[id]["passenger"]
    def getTrips(self,id):
        return self._passenger_registry[id]["trips"]
    def checkPassengerRegistry(self,id):
        if id in self._passenger_registry:
            return True
        else:
            return False
        
        