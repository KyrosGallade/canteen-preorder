from flask import Flask, render_template, request, url_for
import sqlite3

app = Flask(__name__)

def insert_into_db(stall, item, quantity, requests):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(f"""
    INSERT INTO OrderDetail (Order_Stall, Order_Item, Quantity, Requests) 
    VALUES ({stall}, '{item}', {quantity}, '{requests}');
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

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
