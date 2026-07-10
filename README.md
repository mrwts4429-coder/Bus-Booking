# 🚌 Cloud Bus Pass System

A simple Bus Ticket Booking System built with **Python**, **Streamlit**, and **SQLite**.

This application allows users to book bus tickets, search for bookings, view all bookings, and delete bookings through an easy-to-use web interface.

---

## 🚀 Features

- ✅ Book a new bus ticket
- ✅ Calculate ticket price automatically
- ✅ Store bookings in an SQLite database
- ✅ View all bookings
- ✅ Search for a booking by Booking ID
- ✅ Delete a booking
- ✅ Input validation
- ✅ Simple and user-friendly interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLite3
- Pandas
- Random Module

---

## 📂 Project Structure

```
Cloud-Bus-Pass-System/
│
├── ticket.py
├── bus_booking.db
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Cloud-Bus-Pass-System.git
```

### 2. Open the project folder

```bash
cd Cloud-Bus-Pass-System
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

or

```bash
pip install streamlit pandas
```

### 4. Run the application

```bash
streamlit run ticket.py
```

---


## 📋 Database Schema

| Column | Type |
|--------|------|
| booking_id | TEXT |
| passenger_name | TEXT |
| from_city | TEXT |
| to_city | TEXT |
| travel_date | TEXT |
| number_seats | INTEGER |
| total_price | REAL |

---

## 🎯 Future Improvements

- Update/Edit Booking
- Download ticket as PDF
- User Login & Authentication
- Admin Dashboard
- Payment Integration
- Better UI Design

---

## 👩‍💻 Author

**Marwa Sayed Hassan**

Computer Science Student

- LinkedIn: [https://www.linkedin.com/in/your-profile](https://www.linkedin.com/in/marwa-sayed-hassan-b19930336?utm_source=share_via&utm_content=profile&utm_medium=member_android)
- GitHub: https://github.com/mrwts4429-coder
