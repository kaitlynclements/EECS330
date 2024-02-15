'''
    Author: Kaitlyn Clements
    KUID: 3072622
    Lab: 7
'''
# Hashing with seperate chaining
# Each location/bucket can be used to store multiple data objects organized using an auxilary data structure. 
# Each bucket in the hash table will then hold a pointer pointing to one of auxillary data structures
# such as LinkedList, List, Array, etc.


# A. Implementation of HashMap
class HashMap:
    def __init__(self, size):
        self.size = size
        # self.value = value **This would not work because there is no value parameter
        self.hash_table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size
    
    # A.1 Insert a hash key,value in HashMap
    def put(self, key, value):
        """Implement your insertion algo."""
        hash_key = self._hash_function(key)
        self.hash_table[hash_key].append((key, value))
        
    # A.2 Retrieve a value in HashMap
    def get(self, key):
        """Return Corresponding value for Key"""
        hash_key = self._hash_function(key)
        for k, v in self.hash_table[hash_key]:
            if k == key:
                return v
        return None
        
    # A.3 Remove a value in HashMap
    def remove(self, key, value) :
        """Remove Corresponding value for Key"""
        hash_key = self._hash_function(key)
        for pair in self.hash_table[hash_key]:
            if pair[0] == key:
                self.hash_table[hash_key].remove(pair)
        # value was in skeleton code parameters, but you don't need it
        
    # A.4 Display List corresponding to a Key in HashMap
    def display(self):
        """Display the updated hash map"""
        return self.hash_table


    # B. Trip with maximum number of passengers on flight
    # Imagine that we have a list of every commercial airline flight and its corresponding set of trips, 
    # stored as a List. Each flight object stores a flight number, trip id, and a number of passengers on that trip
    # Flight number -> Int(Hash Key)Trip if -> Alpha Numeric (Value1) No.of Passenger -> Int(Value2)
class FlightNode:
    def __init__(self, flight_number, trip_id, passengers):
        self.flight_number = flight_number
        self.trip_id = trip_id
        self.passengers = passengers
        #Implement an algorithm using the HashMap implementation for finding the trip with largest
        # number of passengers on the specified flight
def max_passengers_in_flight(flight_number, hash_map):
    max_passengers = 0
    max_trip_id = None
    hash_key = hash_map._hash_function(flight_number)
    for flight in hash_map.hash_table[hash_key]:
        if flight[0] == flight_number:
            if flight[1].passengers > max_passengers:
                max_passengers = flight[1].passengers
                max_trip_id = flight[1].trip_id
    return (max_trip_id, max_passengers) if max_trip_id is not None else None
    
# Testing logic
# Display the hash map
my_hash_map = HashMap(7)
0, 1, 4, 9, 16, 25, 36, 49, 64, 81
my_hash_map.put("aaa", 0)
my_hash_map.put("bbb", 1)
my_hash_map.put("ccc", 4)
my_hash_map.put("ddd", 9)
my_hash_map.put("eee", 16)
my_hash_map.put("fff", 25)
my_hash_map.put("ggg", 36)
my_hash_map.put("hhh", 49)
my_hash_map.put("ccc", 64)
my_hash_map.put("ccc", 81)
my_hash_map.display()  

# Retrieve values
print("Retrieve values:")
print("aaa:", my_hash_map.get("aaa"))  
print("bbb:", my_hash_map.get("bbb"))
print("ccc:", my_hash_map.get("ccc"))

# Remove a key-value pair
my_hash_map.remove("bbb", 1)  

# Display the updated hash map
my_hash_map.display() 

#Max Passengers on Trip
my_map = HashMap(11)
# Add flight nodes (flight_number, trip_id, passengers)
my_map.put(16, FlightNode(16, "Trip 1", 300))
my_map.put(16, FlightNode(16, "Trip 2", 700))
my_map.put(29, FlightNode(29, "Trip 1", 800))
my_map.put(29, FlightNode(29, "Trip 2", 250))
my_map.put(36, FlightNode(29, "Trip 3", 500))
my_map.put(36, FlightNode(36, "Trip 1", 500))
my_map.put(36, FlightNode(36, "Trip 2", 340))
my_map.put(36, FlightNode(36, "Trip 3", 900))
my_map.put(36, FlightNode(36, "Trip 4", 400))
my_map.put(49, FlightNode(49, "Trip 1", 250))
my_map.put(49, FlightNode(49, "Trip 2", 550))

max_passengers = max_passengers_in_flight(49, my_map)
if max_passengers is not None:
    print("Largest number of people in flight at once :", max_passengers)
else:
    print("Flight not found in the map")
