# Cse-project-vityarthi
 A simple and interactive console-based movie ticket booking system built using Python.

# 🎬 Python Cinema – Movie Ticket Booking System

A simple and interactive **Movie Ticket Booking System** built using Python and NumPy.
Users can view available seats, select multiple seats, get seat-wise pricing, and receive an automatically generated **BookingReceipt.txt** after successful booking.

---

## 📌 Features

* ✔ Displays real-time theater seating layout
* ✔ Dynamic seat pricing based on row
* ✔ Allows multiple seat booking at once
* ✔ Auto-generated unique **Order ID**
* ✔ Neat booking summary after checkout
* ✔ Generates a clean and formatted **BookingReceipt.txt**
* ✔ Uses UTF-8 encoding (supports emojis 🎬🍿)
* ✔ Automatically ends after booking (no need to type “exit”)

---

## 🎥 Seating Layout Format

The theater has **8 rows (A–H)** and **10 seats per row**:

```
H1 H2 H3 H4 H5 H6 H7 H8 H9 H10
G1 G2 G3 G4 G5 G6 G7 G8 G9 G10
F1 F2 F3 F4 F5 F6 F7 F8 F9 F10
E1 E2 E3 E4 E5 E6 E7 E8 E9 E10
D1 D2 D3 D4 D5 D6 D7 D8 D9 D10
C1 C2 C3 C4 C5 C6 C7 C8 C9 C10
B1 B2 B3 B4 B5 B6 B7 B8 B9 B10
A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
```

---

## 💰 Seat Pricing

Each row has its own price:

| Row  | Price (₹) |
| ---- | --------- |
| H, G | 400       |
| F, E | 350       |
| D, C | 300       |
| B, A | 250       |

---

## 🧾 What the User Receives

After booking, the script displays a **booking summary** and creates:

```
BookingReceipt.txt
```

The receipt contains:

* Customer name
* Order ID
* Date & time
* List of booked seats with price
* Total payable amount

---

## 📄 Sample Receipt (BookingReceipt.txt)

```
🎬 Python Cinema – Ticket Receipt 🎬
---------------------------------------------------
Customer Name: Shrishty
Order ID: ORD58291
Date: 2025-11-24 11:45:21

Booked Seats:
  - A1 : Rs 250
  - A2 : Rs 250

TOTAL AMOUNT: Rs 500
---------------------------------------------------
Thank you for booking with Python Cinema! 🍿
```

---

## ▶ How to Run the Program

1. Install **Python 3.x**
2. Install NumPy (if not installed):

```bash
pip install numpy
```

3. Run the script:

```bash
python MovieBooking.py
```

4. Enter your name
5. Enter seats to book (example: `A1 A2 B3`)
6. Check the on-screen summary
7. Find the generated:

```
BookingReceipt.txt
```

---

## 🛠 Technologies Used

* Python
* NumPy
* File handling

---

## 📦 Possible Future Upgrades

* Save booked seats permanently using a file
* Add multiple movies and showtimes
* Add GUI (Tkinter)
* Add PDF receipt export
* Add admin panel for managing seats

---

