from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)

def insert_into_db(stall, item, quantity, requests):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO OrderDetail (Order_Stall, Order_Item, Quantity, Requests, COMPLETED) 
    VALUES ({stall}, '{item}', {quantity}, '{requests}', 'NO');
    """)
    conn.commit()
    conn.close()
    return cursor.lastrowid

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order():
    stall = request.form.get("stall")
    item = request.form.get("menu")
    quantity = request.form.get("quantity")
    requests = request.form.get("requests")
    order_id = insert_into_db(stall, item, quantity, requests)
    return render_template("order.html", order_id=order_id)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/owner", methods=["POST"])
def owner():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT StallOwned, AccountUsername, AccountPassword
    FROM LoginDetail;
    """)
    list_of_owners = cursor.fetchall()
    conn.close()
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    for owner in list_of_owners:
        if entered_username == owner[1] and entered_password == owner[2]:
            stall = owner[0]
            conn = sqlite3.connect("orders.db")
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT Order_ID, Order_Stall, Order_Item, Quantity, Requests
            FROM OrderDetail
            WHERE COMPLETED = 'NO' AND Order_Stall = {stall};
            """)
            stall_orders = cursor.fetchall()
            conn.close()
            return render_template("owner.html", stall_orders=stall_orders, stall=stall)
    return render_template("wrong_login.html")

@app.route("/complete", methods=["POST"])
def complete():
    order_id = request.form.get("order_id")
    stall = request.form.get("stall")
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(f"""
    UPDATE OrderDetail SET
        COMPLETED = 'YES'
    WHERE Order_ID = {order_id};
    """)
    conn.commit()
    conn.close()

    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(f"""
    SELECT Order_ID, Order_Stall, Order_Item, Quantity, Requests
    FROM OrderDetail
    WHERE COMPLETED = 'NO' AND Order_Stall = {stall};
    """)
    stall_orders = cursor.fetchall()
    conn.close()
    return render_template("owner.html", stall_orders=stall_orders)

@app.route("/all_orders", methods=["POST"])
def all_orders():
    stall = request.form.get("stall")
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT *
    FROM OrderDetail;
    """)
    list_of_orders = cursor.fetchall()
    conn.close()
    return render_template("all_orders.html", list_of_orders=list_of_orders)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
