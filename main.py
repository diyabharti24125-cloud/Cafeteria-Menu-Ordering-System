from tkinter import *
from tkinter import messagebox
import mysql.connector
from db_connect import get_connection
from reportlab.pdfgen import canvas

# ---------- Fetch menu from database ----------
def fetch_menu():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT item_id, item_name, price FROM menu")
    data = cursor.fetchall()
    conn.close()
    return data

# ---------- Add item to order ----------
def add_to_order():
    try:
        selected = listbox_menu.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select an item to add!")
            return

        index = selected[0]
        item = menu_data[index]

        quantity = int(entry_qty.get())
        if quantity <= 0:
            messagebox.showwarning("Warning", "Quantity must be > 0!")
            return

        total = item[2] * quantity
        listbox_order.insert(END, f"{item[1]} x{quantity} = ₹{total}")

        global bill_total
        bill_total += total

        label_total.config(text=f"Total Bill: ₹{bill_total}")

        # Store order details
        order_items.append((item[1], quantity, total))

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")

# ---------- Confirm order (save to DB) ----------
def confirm_order():
    if not order_items:
        messagebox.showinfo("Empty", "No items added yet!")
        return

    conn = get_connection()
    cursor = conn.cursor()

    for item in order_items:
        cursor.execute("INSERT INTO orders (item_name, quantity, total_price) VALUES (%s, %s, %s)", item)

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Order saved successfully!")

    # Reset UI
    listbox_order.delete(0, END)
    global bill_total
    bill_total = 0
    label_total.config(text="Total Bill: ₹0")
    order_items.clear()

# ---------- Print Bill as PDF ----------
def print_bill_pdf():
    if not order_items:
        messagebox.showwarning("Warning", "No items to print!")
        return

    file = "bill.pdf"
    c = canvas.Canvas(file)
    c.setFont("Helvetica", 14)

    c.drawString(180, 780, "CAFE DELIGHT CAFETERIA BILL")
    c.setFont("Helvetica", 12)
    c.drawString(50, 760, "---------------------------------------------")

    y = 740
    for item_name, qty, total in order_items:
        c.drawString(50, y, f"{item_name} x{qty} = Rs.{total}")
        y -= 20

    c.drawString(50, y - 10, "---------------------------------------------")
    c.drawString(50, y - 40, f"TOTAL BILL: Rs.{bill_total}")
    c.drawString(50, y - 70, "Thank you! Visit Again :) ")

    c.save()
    messagebox.showinfo("Bill Saved", "Bill saved as bill.pdf (ready to print)")

# ---------- Main GUI ----------
root = Tk()
root.title("Cafeteria Menu Ordering System")
root.geometry("700x500")
root.config(bg="#fff8e1")

menu_data = fetch_menu()
order_items = []
bill_total = 0

# Menu Frame
frame_menu = Frame(root, bg="#e3f2fd", bd=3, relief=RIDGE)
frame_menu.place(x=30, y=50, width=300, height=400)

Label(frame_menu, text="Available Menu", font=("Arial", 14, "bold"), bg="#2196f3", fg="white").pack(fill=X)
listbox_menu = Listbox(frame_menu, font=("Arial", 12))
for item in menu_data:
    listbox_menu.insert(END, f"{item[1]}  -  ₹{item[2]}")
listbox_menu.pack(fill=BOTH, expand=True, pady=10, padx=10)

# Order Frame
frame_order = Frame(root, bg="#fff3e0", bd=3, relief=RIDGE)
frame_order.place(x=370, y=50, width=300, height=400)

Label(frame_order, text="Your Order", font=("Arial", 14, "bold"), bg="#ff9800", fg="white").pack(fill=X)
listbox_order = Listbox(frame_order, font=("Arial", 12))
listbox_order.pack(fill=BOTH, expand=True, pady=10, padx=10)

# Controls
Label(root, text="Quantity:", font=("Arial", 12), bg="#fff8e1").place(x=40, y=460)
entry_qty = Entry(root, width=5)
entry_qty.place(x=120, y=460)

Button(root, text="Add Item", command=add_to_order, bg="#43a047", fg="white",
       font=("Arial", 11, "bold")).place(x=200, y=455)

Button(root, text="Confirm Order", command=confirm_order, bg="#e53935", fg="white",
       font=("Arial", 11, "bold")).place(x=330, y=455)

Button(root, text="Print Bill (PDF)", bg="#6a1b9a", fg="white",
       font=("Arial", 11, "bold"), command=print_bill_pdf).place(x=500, y=455)

label_total = Label(root, text="Total Bill: ₹0", font=("Arial", 14, "bold"), bg="#fff8e1", fg="#1a237e")
label_total.place(x=500, y=420)

root.mainloop()