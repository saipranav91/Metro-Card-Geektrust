from sys import argv
from src.TripManager import TripManager 
from src.Printing import Printing 
from src.Fare import Fare 
from src.Collection import Collection
from src.Passenger import PassengerFactory


def main():
    filePath=validate_args(argv)
    temp_balance={}
    trip_manager=TripManager() 
    printing=Printing() 
    collection=Collection() 
    fare=Fare()
    passengerFactory=PassengerFactory()
    process_file(filePath,temp_balance,trip_manager,passengerFactory,collection,fare)
    printing.printSummary(trip_manager,collection)


def validate_args(args):
    minimum=2
    if len(args)!=minimum:
        raise Exception("File Path does not exist")
    return args[1]           

def process_file(filePath,temp_balance,trip_manager,passengerFactory,collection,fare):
    with open(filePath,'r') as file:
        lines=file.readlines()
    for line in lines:
        line.strip() 
        if not line:
            break 
        process_line(line, temp_balance, trip_manager, passengerFactory, collection, fare)

def process_line(line,temp_balance,trip_manager,passengerFactory,collection,fare):
    line=line.split(" ")
    if line[0]=="BALANCE":
        process_balance(line,temp_balance)
    elif line[0]=="CHECK_IN":
        process_check_in(line,temp_balance,trip_manager,passengerFactory,collection,fare)

def process_balance(line,temp_balance):
    passenger_id=line[1]
    balance=int(line[2])
    temp_balance[passenger_id]=balance 
     

def process_check_in(line,temp_balance,trip_manager,passengerFactory,collection,fare):
    id = line[1]
    passenger_type = line[2]
    starting_point = line[3].strip()
    if not trip_manager.checkPassengerRegistry(id):
        passenger=passengerFactory.createPassenger(id,temp_balance[id],passenger_type)
        trip_manager.addRegistry(id,passenger)
    else:
        passenger=trip_manager.getPassenger(id)
        trip_manager.updateTrips(id)
    trip_manager.updateSummary(starting_point,passenger_type)
    collection.controlCollection(passenger,fare,trip_manager,starting_point)


            