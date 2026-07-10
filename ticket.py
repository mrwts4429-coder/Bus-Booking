import streamlit as st
import sqlite3
import random
import pandas as pd

def get_connection():
    return sqlite3.connect("bus_booking.db")

st.set_page_config(
    page_title="Cloud Bus Pass System",
    page_icon="🚌",
    layout="centered"
)

st.title("Cloud Bus Pass System 🚌")

st.caption("Book your bus ticket easily")

st.info("Fill in the form below to book your ticket.")

st.divider()

passenger_name = st.text_input("Passenger Name")

from_city = st.selectbox(
    "From",
    [
        "Cairo",
        "Alexandria",
        "Assiut",
        "Sohag"
    ]
)

to_city = st.selectbox(
    "To",
    [
        "Cairo",
        "Alexandria",
        "Assiut",
        "Sohag"
    ]
)

travel_date = str(st.date_input("Travel Date"))

number_seats = st.number_input(
    "Number Seats",
    min_value=1,
    value=1,
    step=1
)

prices = {
    ("Cairo", "Alexandria"): 100,
    ("Alexandria", "Cairo"): 100,

    ("Cairo", "Assiut"): 180,
    ("Assiut", "Cairo"): 180,

    ("Assiut", "Sohag"): 90,
    ("Sohag", "Assiut"): 90,

    ("Alexandria", "Sohag"): 250,
    ("Sohag", "Alexandria"): 250
}

conn = get_connection()
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS bookings(
               booking_id      TEXT PRIMARY KEY,
               passenger_name  TEXT,
               from_city       TEXT,
               to_city         TEXT,
               travel_date     TEXT,
               number_seats    INTEGER,
               total_price     REAL
               )
               """)
conn.commit()
conn.close()
book_button = st.button("Book Ticket 🚌")

if book_button:

    if passenger_name == "":
        st.error("Please enter passenger name.")

    elif from_city == to_city:
        st.error("From and To cannot be the same.")

    elif number_seats < 1:
        st.error("Please Enter Number From 1")

    elif (from_city, to_city) not in prices:
        st.error("This route is not available.")

    else:
        price = prices[(from_city, to_city)]
        total_price = price * number_seats
        booking_id = f"BUS{random.randint(1000,9999)}"

        conn = get_connection()    
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO bookings VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                booking_id,
                passenger_name,
                from_city,
                to_city,
                travel_date,
                number_seats,
                total_price
            )
        )

        conn.commit()
        conn.close()

        st.success("✅ Ticket booked successfully!")

        st.markdown(f"## 🎫 Ticket #{booking_id}")

        st.info(f"""
👤 Passenger: {passenger_name}

📍 From: {from_city}

🏁 To: {to_city}

📅 Travel Date: {travel_date}

💺 Number of Seats: {number_seats}

💰 Total Price: {total_price} EGP
""")
view_button = st.button("📋 View All Bookings")

if view_button:
    conn = get_connection()  
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    all_bookings_df = pd.DataFrame(
    rows,
    columns=[
        "Booking ID",
        "Passenger Name",
        "From",
        "To",
        "Travel Date",
        "Seats",
        "Total Price"
    ]
)
    if not rows:
        st.warning("No bookings found.")
    else:
        st.dataframe(all_bookings_df)
        conn.close()
st.divider()

st.subheader("🔍 Search Booking")
search_booking = st.text_input("Enter Booking ID")
search_button = st.button("🔍 Search")
if search_button:
    conn = get_connection() 
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM bookings WHERE booking_id = ?",
        (search_booking,)
        )
    row = cursor.fetchone()
    if row is None:
        st.error("Booking not found.")
    else:
        st.success("✅ Booking Found!")

        st.markdown(f"## 🎫 Ticket #{row[0]}")

        st.info(f"""
        👤 Passenger: {row[1]}

        📍 From: {row[2]}

        🏁 To: {row[3]}

        📅 Travel Date: {row[4]}

        💺 Number of Seats: {row[5]}

        💰 Total Price: {row[6]} EGP
        """)
        conn.close()
st.divider()
st.subheader("Delete Booking 🗑️")
Delete_booking = st.text_input(
    "Enter Booking ID to Delete"
)
Delete_button = st.button("Delete🗑️")
if Delete_button:
    if not Delete_booking:
        st.error("Please enter Booking ID.")
    else:
        conn = get_connection()  
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM bookings WHERE booking_id = ?",
            (Delete_booking,)
            )
        if cursor.rowcount == 0:
            st.error("Booking not found.")
        else:
            st.success("Ticket deleted successfully.")
            st.balloons()
        conn.commit()
        conn.close()
        

