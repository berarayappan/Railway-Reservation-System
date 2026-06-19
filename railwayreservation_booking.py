from collections import deque


class Passenger:

    def __init__(
        self,
        passenger_id,
        name,
        age,
        gender,
        preferred_berth
    ):

        self.passenger_id = passenger_id
        self.name = name
        self.age = age
        self.gender = gender
        self.preferred_berth = preferred_berth

        self.allotted_berth = None
        self.seat_number = None


class RailwayReservation:

    def __init__(self):

        self.lower = [1, 2, 3, 4, 5]
        self.middle = [1, 2, 3, 4, 5]
        self.upper = [1, 2, 3, 4, 5]
        self.side_lower = [1, 2, 3]
        self.side_upper = [1, 2]

        self.booked = {}

        self.rac = deque()
        self.RAC_LIMIT = 2

        self.waiting = deque()
        self.WAITING_LIMIT = 2

    def bookTicket(self, passenger):
        
        if passenger.age < 5:

           print("No Berth Allocated for Child Below 5 Years")

           return
        preferred = passenger.preferred_berth

        if preferred == "LOWER":

          if len(self.lower) > 0:

            seat = self.lower.pop(0)

            passenger.allotted_berth = "LOWER"
            passenger.seat_number = seat

            self.booked[passenger.passenger_id] = passenger

            print("Ticket Booked Successfully")
            print("Berth :", passenger.allotted_berth)
            print("Seat No :", passenger.seat_number)

          else:

            if len(self.rac) < self.RAC_LIMIT:

              self.rac.append(passenger)

              print("No Berth Available")
              print("Passenger Added To RAC")

            else:

              if len(self.waiting) < self.WAITING_LIMIT:

                self.waiting.append(passenger)

                print("RAC Full")
                print("Passenger Added To Waiting List")

              else:

                print("No Tickets Available")
        elif preferred == "MIDDLE":

          if len(self.middle) > 0:

            seat = self.middle.pop(0)

            passenger.allotted_berth ="MIDDLE"
            passenger.seat_number = seat

            self.booked[passenger.passenger_id] = passenger

            print("Ticket Booked Successfully")
            print("Berth :", passenger.allotted_berth)
            print("Seat No :", passenger.seat_number)

          else:
           
            if len(self.rac) < self.RAC_LIMIT:

              self.rac.append(passenger)

              print("No Berth Available")
              print("Passenger Added To RAC")

            else:

              if len(self.waiting) < self.WAITING_LIMIT:

                self.waiting.append(passenger)
                
                print("RAC Full")
                print("Passenger Added to Waiting List")

              else:
                print("No tickets available")

        elif preferred == "UPPER":

          if len(self.upper) > 0:

            seat = self.upper.pop(0)

            passenger.allotted_berth ="UPPER"
            passenger.seat_number = seat

            self.booked[passenger.passenger_id] = passenger

            print("Ticket Booked Successfully")
            print("Berth :", passenger.allotted_berth)
            print("Seat No :", passenger.seat_number)

          else:
              if len(self.rac) < self.RAC_LIMIT:

                self.rac.append(passenger)

                print("No berth Available")
                print("Passenger Added To RAC")

              else:

                if len (self.waiting) < self.WAITING_LIMIT:

                  self.waiting.append(passenger)

                  print("RAC full")
                  print("Passenger added to Waiting List")

                else:
                  print("No tickets available")


        elif preferred == "SIDE_LOWER":

          if len(self.side_lower) > 0:

            seat = self.side_lower.pop(0)

            passenger.allotted_berth ="SIDE_LOWER"
            passenger.seat_number = seat

            self.booked[passenger.passenger_id] = passenger

            print("Ticket Booked Successfully")
            print("Berth :", passenger.allotted_berth)
            print("Seat No :", passenger.seat_number)

          else:

            if len(self.rac) < self.RAC_LIMIT:

              self.rac.append(passenger)

              print("No Berth Available")
              print("Passenger Added To RAC")

            else:

              if len(self.waiting) < self.WAITING_LIMIT:
                self.waiting.append(passenger)

                print("RAC Full")
                print("Passenger Added to Waiting List")

              else:
                print("No available tickets")

        elif preferred == "SIDE_UPPER":

          if len(self.side_upper) > 0:

            seat = self.side_upper.pop(0)

            passenger.allotted_berth ="SIDE_UPPER"
            passenger.seat_number = seat

            self.booked[passenger.passenger_id] = passenger

            print("Ticket Booked Successfully")
            print("Berth :", passenger.allotted_berth)
            print("Seat No :", passenger.seat_number)

          else:

            if len(self.rac) < self.RAC_LIMIT:

              self.rac.append(passenger)

              print("No Berth Available")
              print("Passenger Added To RAC")

            else:

              if len(self.waiting) < self.WAITING_LIMIT:

                self.waiting.append(passenger)

                print("RAC Full")
                print("Passenger added to Waiting List")

              else:
                print("No tickets available")


    def printRAC(self):

      print("\n===== RAC LIST =====")

      if len(self.rac) == 0:
        print("No RAC Passengers")
        return

      for passenger in self.rac:

        print(
            passenger.passenger_id,
            passenger.name
        ) 
        

    def printWaitingList(self):

      print("\n===== WAITING LIST =====")

      if len(self.waiting) == 0:

        print("No Waiting Passengers")
        return

      for passenger in self.waiting:

        print(
            passenger.passenger_id,
            passenger.name
        )
    def cancelTicket(self, passenger_id):

      if passenger_id not in self.booked:

        print("Passenger Not Found")
        return

      passenger = self.booked[passenger_id]

      berth = passenger.allotted_berth
      seat = passenger.seat_number

      print("Berth =", berth)
      print("Seat =", seat)

      del self.booked[passenger_id]

    # 👇 STEP 5 START

      if berth == "LOWER":

        self.lower.append(seat)
        self.lower.sort()

      elif berth == "MIDDLE":

        self.middle.append(seat)
        self.middle.sort()

      elif berth == "UPPER":

        self.upper.append(seat)
        self.upper.sort()

      elif berth == "SIDE_LOWER":

        self.side_lower.append(seat)
        self.side_lower.sort()

      elif berth == "SIDE_UPPER":

        self.side_upper.append(seat)
        self.side_upper.sort()

    # 👆 STEP 5 END

      print("Ticket Cancelled Successfully")

      if len(self.rac) > 0:

        rac_passenger = self.rac.popleft()

        rac_passenger.allotted_berth = berth
        rac_passenger.seat_number = seat

        self.booked[rac_passenger.passenger_id] = rac_passenger

        print(
          rac_passenger.name,
          "Moved From RAC To Confirmed Ticket"
        )

      if len(self.waiting) > 0:

        waiting_passenger = self.waiting.popleft()

        self.rac.append(waiting_passenger)

        print(
          waiting_passenger.name,
          "Moved From Waiting To RAC"
       )
    def printBookedTickets(self):
        for passenger in self.booked.values():

          print("\nPassenger ID :", passenger.passenger_id)
          print("Name :", passenger.name)
          print("Age :", passenger.age)
          print("Gender :", passenger.gender)
          print("Berth :", passenger.allotted_berth)
          print("Seat No :", passenger.seat_number)
          

    def printAvailableTickets(self):
        print("\nAvailable Tickets")

        print("Lower List =", self.lower)

        print("Lower :", len(self.lower))
        print("Middle :", len(self.middle))
        print("Upper :", len(self.upper))
        print("Side Lower :", len(self.side_lower))
        print("Side Upper :", len(self.side_upper))
        
    
rr = RailwayReservation()

p1 = Passenger(
    101,
    "Ram",
    25,
    "Male",
    "LOWER"
)

p2 = Passenger(
    102,
    "Ravi",
    30,
    "Male",
    "MIDDLE"
)

p3 = Passenger(
    103,
    "Sri",
    45,
    "Female",
    "UPPER"
)

p4 = Passenger(
    104,
    "SriRam",
    46,
    "Female",
    "SIDE_LOWER"
)

p5 = Passenger(
    105,
    "Sriguru",
    50,
    "Male",
    "SIDE_UPPER"
)

p6 = Passenger(
    106,
    "Baby",
    3,
    "Male",
    "LOWER"
)

p10 = Passenger(
    110,
    "Kumar",
    25,
    "Male",
    "LOWER"
)

p11 = Passenger(
    111,
    "Arun",
    28,
    "Male",
    "LOWER"
)

p12 = Passenger(
    112,
    "Karthik",
    29,
    "Male",
    "LOWER"
)

p13 = Passenger(
    113,
    "Vijay",
    30,
    "Male",
    "LOWER"
)

p14 = Passenger(
    114,
    "Ajith",
    31,
    "Male",
    "LOWER"
)



rr = RailwayReservation()

rr.bookTicket(p1)   # Confirmed

rr.lower = []

rr.bookTicket(p10)  # RAC
rr.bookTicket(p11)  # RAC

rr.bookTicket(p12)  # Waiting
rr.bookTicket(p13)  # Waiting

rr.cancelTicket(101)



