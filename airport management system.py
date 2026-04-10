import pickle

FILE_NAME =("flights.dat")

try:
    with open(FILE_NAME, "rb") as f:
        flights = pickle.load(f)
except FileNotFoundError:
    flights = []

def save_flights():
    with open(FILE_NAME, "wb") as f:
        pickle.dump(flights, f)

def add_flight():
    flightno = int(input("Enter Flight Number: "))
    source = input("Enter Source: ")
    destination = input("Enter Destination: ")
    seats = int(input("Enter Seats: "))
    flights.append({
        "flightno": flightno,
        "source": source,
        "destination": destination,
        "seats": seats
    })
    save_flights()
    print("Flight Added Successfully!")

def view_flights():
    if not flights:
        print("No flights available.")
        return
    for f in flights:
        print(f"Flight No: {f['flightno']}, Source: {f['source']}, Destination: {f['destination']}, Seats: {f['seats']}")

def search_flight():
    num = int(input("Enter Flight Number: "))
    for f in flights:
        if f['flightno'] == num:
            print("Flight Found:", f)
            return
    print("Flight Not Found!")
    
def update_flight():
    num = int(input("Enter Flight Number to Update: "))
    for f in flights:
        if f['flightno'] == num:
            print("Current Flight Details:", f)
            f['source'] = input("Enter new Source: ")
            f['destination'] = input("Enter new Destination: ")
            f['seats'] = int(input("Enter new Seats: "))
            save_flights()
            print("Flight Updated Successfully!")
            return
    print("Flight Not Found!")

def delete_flight():
    num = int(input("Enter Flight Number to Delete: "))
    for i, f in enumerate(flights):
        if f['flightno'] == num:
            print("Deleting Flight:", f)
            flights.pop(i)
            save_flights()
            print("Flight Deleted Successfully!")
            return
    print("Flight Not Found!")

def book_seat():
    num = int(input("Enter Flight Number: "))
    for f in flights:
        if f['flightno'] == num:
            seats = int(input("Enter Seats to Book: "))
            if f['seats'] >= seats:
                f['seats'] -= seats
                save_flights()
                print("Booking Successful! Remaining Seats:", f['seats'])
            else:
                print("Not Enough Seats!")
            return
    print("Flight Not Found!")

# Menu
while True:
    print("\n1. Add Flight\n2. View Flights\n3. Search Flight\n4. update_flight()\n5. delete_flight()\n6. book_seat()\n7. Exit")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        add_flight()
    elif ch == 2:
        view_flights()
    elif ch == 3:
        search_flight()
    elif ch == 4:
         update_flight()
    elif ch == 5:
        delete_flight()
    elif ch == 6:
        book_seat()
    elif ch == 7:       
        print("Thank you!")
        print("Happy journey!")
        break
    else:
        print("Invalid Choice!")