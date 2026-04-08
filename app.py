from flask import Flask,render_template,session,request,url_for,redirect
from db_connection import get_db_connection
import os
import mysql.connector



app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
@app.route("/")
def home():
    conn = get_db_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM products")
    results = c.fetchall()
    conn.close()
    return render_template("home.html",products = results)


@app.route("/product/<int:id>")
def product_details(id):
    conn = get_db_connection()
    
    
    c = conn.cursor()
    identity = id
    print(identity)
    c.execute("SELECT product_id, product_name,product_description FROM products WHERE product_id = ?",(identity,))
    result = c.fetchone()
    print(result)
    conn.close()
    return render_template("render.html",products = result)

@app.route("/add-to-cart",methods = ["POST"])
def add_to_cart():
    product_id = request.form.get("product_id")
 # Step 1: validate input
    if not product_id:
        return redirect(url_for("home"))

    product_id = int(product_id)  # convert to int

    # Step 2: initialize cart if not exists
    if "cart" not in session:
        session["cart"] = []

    # Step 3: add item
    cart = session["cart"]
    cart.append(product_id)

    # Step 4: IMPORTANT → reassign to trigger session update
    session["cart"] = cart

    print(session)

    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    if "cart" not in session:
        return "Cart is empty.Please add something."

    conn = get_db_connection()
    c = conn.cursor()
    items = session.get("cart")
    print(items)
    if items:
        placeholders = ",".join(["?"] * len(items))
        query = f"SELECT product_name,product_description FROM products WHERE product_id IN ({placeholders})"
        c.execute(query,items)
        results = c.fetchall()
        conn.close()
        return render_template("cart.html",cart_items = results)
    return "hi"


    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
