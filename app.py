from flask import Flask, render_template, request ,redirect, url_for, session,jsonify
import mysql.connector
import os
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Change this to a random secret key
CORS(app)


db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT", 3306))
)

cursor = db.cursor(dictionary=True)




@app.route("/")
def home():

    cursor.execute("SELECT * FROM food LIMIT 8")

    foods = cursor.fetchall()
    print(foods)  

    return render_template("index.html", foods=foods)
@app.route("/register",methods=["GET","POST"])
@app.route("/api/foods", methods=["GET"])
def api_foods():

    cursor.execute("SELECT * FROM food")

    foods = cursor.fetchall()

    return jsonify(foods)

def register():

    if request.method=="POST":

        fullname=request.form["fullname"]

        email=request.form["email"]

        phone=request.form["phone"]

        password=request.form["password"]

        cursor.execute(

        "SELECT * FROM users WHERE email=%s",

        (email,)

        )

        user=cursor.fetchone()

        if user:

            return "Email Already Exists"

        cursor.execute(

        """
        INSERT INTO users(fullname,email,phone,password)

        VALUES(%s,%s,%s,%s)

        """,

        (fullname,email,phone,password)

        )

        db.commit()

        return "Registration Successful"

    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cursor.fetchone()

        if user:
            session["user"] = user["fullname"]
            session["user_id"] = user["id"]
            session["user_name"] = user["fullname"]

            return redirect(url_for("home"))

        else:
            return "Invalid Email or Password"

    return render_template("login.html")
@app.route("/api/login", methods=["POST"])
def api_login():

    data = request.get_json()

    email = data["email"]
    password = data["password"]

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cursor.fetchone()

    if user:

        return jsonify({
            "success": True,
            "user": {
                "id": user["id"],
                "fullname": user["fullname"],
                "email": user["email"]
            }
        })
    return jsonify({
        "success": False,
        "message": "Invalid Email or Password"
    }), 401
@app.route("/api/place_order", methods=["POST"])
def api_place_order():
    try:

        data = request.get_json()

        user_id = data["user_id"]
        customer_name = data["customer_name"]
        phone = data["phone"]
        address = data["address"]
        payment_method = data["payment_method"]
        total_amount = data["total_amount"]
        items = data["items"]

        # Insert into orders table
        cursor.execute("""
            INSERT INTO orders
            (user_id, customer_name, phone, address,
             payment_method, total_amount)
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            user_id,
            customer_name,
            phone,
            address,
            payment_method,
            total_amount
        ))

        db.commit()

        # Get newly created order id
        order_id = cursor.lastrowid

        # Insert each ordered food
        for item in items:

            cursor.execute("""
                INSERT INTO order_items
                (order_id, food_id, food_name, quantity, price)
                VALUES (%s,%s,%s,%s,%s)
            """, (
                order_id,
                item["food_id"],
                item["food_name"],
                item["quantity"],
                item["price"]
            ))

        db.commit()

        return jsonify({
            "success": True,
            "message": "Order placed successfully",
            "order_id": order_id
        })

    except Exception as e:

        db.rollback()

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500
#logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

#add to cart route
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):

    cursor.execute(
        "SELECT * FROM food WHERE id=%s",
        (id,)
    )

    food = cursor.fetchone()

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    found = False

    for item in cart:

        if item["id"] == food["id"]:

            item["quantity"] += 1

            found = True

            break

    if not found:

        food["quantity"] = 1

        cart.append(food)

    session["cart"] = cart

    return redirect("/")
#view cart route
@app.route("/cart")
def cart():

    cart = session.get("cart", [])

    total = 0

    for item in cart:
       total += float(item["price"]) * item["quantity"]

    return render_template(
        "cart.html",
        cart=cart,
        total=total
    )
#remove item from cart
@app.route("/remove/<int:id>")
def remove(id):

    cart = session.get("cart", [])

    cart = [item for item in cart if item["id"] != id]

    session["cart"] = cart

    return redirect("/cart")
#clear cart route
@app.route("/clear_cart")
def clear_cart():
    session.pop("cart", None)
    return "Cart Cleared!"
#chekout route
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        customer_name = request.form["customer_name"]
        phone = request.form["phone"]
        address = request.form["address"]

        user_id = session.get("user_id")   # Get logged-in user ID

        cart = session.get("cart", [])

        total = 0

        for item in cart:
            total += float(item["price"])

        cursor.execute("""
            INSERT INTO orders
            (user_id, customer_name, phone, address, total_amount)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                session["user_id"],
                customer_name,
                phone,
                address,
                total
            ))

        db.commit()

        session.pop("cart", None)

        return redirect("/order_success")

    return render_template("checkout.html")
#admin route
@app.route("/admin")
def admin():

    cursor.execute("SELECT * FROM food")

    foods = cursor.fetchall()

    return render_template(
        "admin.html",
        foods=foods
    )
#food add route
@app.route("/add_food", methods=["GET", "POST"])
def add_food():

    if request.method == "POST":

        food_name = request.form["food_name"]

        price = request.form["price"]

        image = request.form["image"]

        cursor.execute(

        """

        INSERT INTO food

        (food_name,price,image)

        VALUES(%s,%s,%s)

        """,

        (food_name,price,image)

        )

        db.commit()

        return redirect("/admin")

    return render_template("add_food.html")
#food delete route
@app.route("/delete_food/<int:id>")
def delete_food(id):

    cursor.execute(

    "DELETE FROM food WHERE id=%s",

    (id,)

    )

    db.commit()

    return redirect("/admin")
#food edit route
@app.route("/edit_food/<int:id>", methods=["GET", "POST"])
def edit_food(id):

    if request.method == "POST":

        food_name = request.form["food_name"]

        price = request.form["price"]

        image = request.form["image"]

        cursor.execute(

        """

        UPDATE food

        SET

        food_name=%s,

        price=%s,

        image=%s

        WHERE id=%s

        """,

        (food_name,price,image,id)

        )

        db.commit()

        return redirect("/admin")

    cursor.execute(

    "SELECT * FROM food WHERE id=%s",

    (id,)

    )

    food = cursor.fetchone()

    return render_template(

    "edit_food.html",

    food=food

    )
#dashboard route
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    cursor.execute(
        "SELECT * FROM orders WHERE user_id=%s",
        (session["user_id"],)
    )

    orders = cursor.fetchall()

    total_spent = sum(float(order["total_amount"]) for order in orders)

    return render_template(
        "dashboard.html",
        orders=orders,
        total_spent=total_spent,
        pending_orders=0,
        delivered_orders=0
    )
#search route
@app.route("/search")
def search():

    search = request.args.get("search")

    cursor.execute(
        "SELECT * FROM food WHERE food_name LIKE %s",
        ("%" + search + "%",)
    )

    foods = cursor.fetchall()

    return render_template("index.html", foods=foods,searched=True)
#increase quantity route
@app.route("/increase/<int:id>")
def increase(id):

    cart = session["cart"]

    for item in cart:

        if item["id"] == id:

            item["quantity"] += 1

            break

    session["cart"] = cart

    return redirect("/cart")
#decrease quantity route
@app.route("/decrease/<int:id>")
def decrease(id):

    cart = session["cart"]

    for item in cart:

        if item["id"] == id:

            if item["quantity"] > 1:

                item["quantity"] -= 1

            else:

                cart.remove(item)

            break

    session["cart"] = cart

    return redirect("/cart")
#order success route
@app.route("/order_success")
def order_success():
    return render_template("order_success.html")


if __name__ == "__main__":
    app.run(debug=True)
