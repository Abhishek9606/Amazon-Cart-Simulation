from flask import Flask,render_template,session,request,url_for,redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "app"

@app.route("/")
def home():
    conn = sqlite3.connect("products.db")
    c = conn.cursor()

    c.execute("SELECT * FROM products")
    results = c.fetchall()
    conn.close()
    return render_template("home.html",products = results)


@app.route("/product/<int:id>")
def product_details(id):
    conn = sqlite3.connect("products.db")
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
    if request.method == "POST":
        product_id = request.form.get("product_id")
        if "cart" not in session:
            session["cart"] = []
        else:
            session["cart"].append(product_id)
            print(session)
            return redirect(url_for("cart"))
    return redirect(url_for("home"))


@app.route("/cart")
def cart():
    if "cart" not in session:
        return "Cart is empty.Please add something."

    conn = sqlite3.connect("products.db")
    c = conn.cursor()
    items = session.get("cart")
    print(items)
    if items:
        placeholders = "".join(["/"] * len(items))
        query = f"SELECT product_name,product_description FROM products WHERE product_id = placholders"
        c.execute(query,items)
        results = c.fetchall()
        conn.close()
        return render_template("cart.html",cart_items = results)
    return "hi"


    
if __name__ == "__main__":
    app.run(debug = True)


