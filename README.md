# Railway Reservation System (Python)

## Overview

This is a console-based Railway Reservation System developed using Python and Object-Oriented Programming concepts.

The project simulates a real-world railway ticket booking process with berth allocation, RAC management, waiting list handling, ticket cancellation, and automatic passenger promotion.

---

## Features

* Ticket Booking
* Lower, Middle, Upper Berth Allocation
* Side Lower and Side Upper Berth Allocation
* RAC (Reservation Against Cancellation)
* Waiting List Management
* Ticket Cancellation
* Automatic RAC to Confirmed Ticket Promotion
* Automatic Waiting List to RAC Promotion
* Child Age Validation (Below 5 years)
* View Booked Tickets
* View Available Tickets
* View RAC Passengers
* View Waiting List Passengers

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

---

## Data Structures Used

* List
* Dictionary
* Queue (deque)

---

## Classes

### Passenger

Stores passenger details such as:

* Passenger ID
* Name
* Age
* Gender
* Preferred Berth
* Allotted Berth
* Seat Number

### RailwayReservation

Handles:

* Ticket Booking
* Ticket Cancellation
* RAC Management
* Waiting List Management
* Passenger Promotion Logic

---

## OOP Concepts Used

* Class
* Object
* Constructor (**init**)
* Encapsulation

---

## Project Workflow

1. Passenger requests a ticket.
2. If berth is available, a confirmed ticket is allocated.
3. If no berth is available, the passenger is moved to RAC.
4. If RAC is full, the passenger is moved to the Waiting List.
5. When a confirmed ticket is cancelled:

   RAC passenger gets the confirmed berth.
   Waiting List passenger moves to RAC.

---

## Author

BERA R
