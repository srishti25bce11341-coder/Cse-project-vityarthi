import numpy as np
import random
import datetime
# Seat layout
arr = np.array([
    ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10"],
    ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10"],
    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10"],
    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10"],
    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10"],
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"],
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"],
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10"]
])
# Prices for each row
price_map = {
    "A": 250,
    "B": 250,
    "C": 300,
    "D": 300,
    "E": 350,
    "F": 350,
    "G": 400,
    "H": 400
}
booked = set()
print("\n🎬 Welcome to Python Cinema Ticket Booking 🎟️")
customer_name = input("Enter your name: ").title()
print("\n=== 🎦 Current Seating Layout ===")
for row in arr:
    print(row)
seats = input("\nEnter seats to book (e.g., A1 A2 B3): ").upper()
seat_list = seats.split()
order_details = []
total_price = 0
for seat in seat_list:
    found = False
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i][j] == seat:
                found = True
                if seat in booked:
                    print(f"❌ Seat {seat} is already booked!")
                else:
                    arr[i][j] = "✓"
                    booked.add(seat)
                    row_letter = seat[0]
                    price = price_map.get(row_letter, 0)
                    order_details.append((seat, price))
                    total_price += price
                    print(f"✔ Seat {seat} booked for Rs {price}.")
                break
        if found:
            break
    if not found:
        print(f"❌ Invalid seat: {seat}")
# Generate Order ID
order_id = "ORD" + str(random.randint(10000, 99999))
print("\n===============================")
print("🧾   BOOKING SUMMARY")
print("===============================")
print(f"Customer Name: {customer_name}")
print(f"Order ID: {order_id}\n")
for s, p in order_details:
    print(f"Seat {s} → Rs {p}")
print(f"\nTOTAL AMOUNT → Rs {total_price}")
print("===============================\n")
# Write receipt
with open("BookingReceipt.txt", "w", encoding="utf-8") as f:
    f.write("        🎬 Python Cinema – Ticket Receipt 🎬\n")
    f.write("---------------------------------------------------\n")
    f.write(f"Customer Name: {customer_name}\n")
    f.write(f"Order ID: {order_id}\n")
    f.write(f"Date: {datetime.datetime.now()}\n\n")
    f.write("Booked Seats:\n")
    for s, p in order_details:
        f.write(f"  - {s} : Rs {p}\n")
    f.write("\n")
    f.write(f"TOTAL AMOUNT: Rs {total_price}\n")
    f.write("---------------------------------------------------\n")
    f.write("Thank you for booking with Python Cinema! 🍿\n")
print("🧾 BookingReceipt generated: BookingReceipt.txt")
print("🎉 Booking completed successfully!")
