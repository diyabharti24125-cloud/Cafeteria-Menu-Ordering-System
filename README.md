# 🍴 Cafeteria Menu Ordering System

## 📘 Objective
To design and implement a simple desktop-based application that allows users to order food items from a menu, calculate the total bill, and store order details in a database using Python and MySQL.

---

## 🧠 Overview
The *Cafeteria Menu Ordering System* is a Python–MySQL integrated application that helps in automating the food ordering process in a cafeteria.  
It provides a user-friendly GUI built with Tkinter, where customers can view menu items, select quantities, and generate bills.  
All orders are stored in a MySQL database for daily sales tracking.

---

## ⚙️ Technologies Used
- *Python 3.x*
- *Tkinter* (for GUI)
- *MySQL* (via XAMPP)
- *mysql-connector-python*
- *VS Code* (IDE)

---

## 🗂️ Database Details
*Database Name:* cafeteria_db

*Tables:*
1. *menu*
   - item_id (INT, Primary Key, Auto Increment)
   - item_name (VARCHAR)
   - category (VARCHAR)
   - price (DECIMAL)

2. *orders*
   - order_id (INT, Primary Key, Auto Increment)
   - item_name (VARCHAR)
   - quantity (INT)
   - total_price (DECIMAL)
   - order_date (DATETIME, Default = Current Timestamp)

---

## 💻 Features
✅ Displays food menu dynamically from the database  
✅ Allows selecting multiple items with quantity  
✅ Calculates total bill automatically  
✅ Saves all orders in MySQL database  
✅ User-friendly interface using Tkinter  
✅ Option to extend with sales reports and login system  

---

## 📋 How to Run the Project

### Step 1: Install Prerequisites
```bash
pip install mysql-connector-python