from flask import Flask, render_template, request ,redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "fooddelivery123" # Change this to a random secret key

db = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="subash1420",
    database="food_delivery"
)

cursor = db.cursor(dictionary=True)

@app.route("/")
def home():

    cursor.execute("SELECT * FROM food")

    foods = cursor.fetchall()
    print(foods)  

    return render_template("index.html", foods=foods)
@app.route("/register",methods=["GET","POST"])

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
#logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))

#add to cart route
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):

    cursor.execute("SELECT * FROM food WHERE id=%s", (id,))
    food = cursor.fetchone()

    if "cart" not in session:
        session["cart"] = []

    cart = session["cart"]

    cart.append(food)

    session["cart"] = cart

    return redirect("/")
#view cart route
@app.route("/cart")
def cart():

    cart = session.get("cart", [])

    total = 0

    for item in cart:
        total += float(item["price"])

    return render_template(
        "cart.html",
        cart=cart,
        total=total
    )
#remove item from cart
@app.route("/remove/<int:index>")
def remove(index):

    cart = session.get("cart", [])

    if index < len(cart):

        cart.pop(index)

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

    if request.method == "POST":

        customer_name = request.form["customer_name"]
        phone = request.form["phone"]
        address = request.form["address"]

        user_id = session.get("user_id")   # Get logged-in user ID

        cart = session.get("cart", [])

        total = 0

        for item in cart:
            total += float(item["price"])

        cursor.execute(
            """
            INSERT INTO orders
            (user_id, customer_name, phone, address, total_amount)

            VALUES(%s,%s,%s,%s,%s)
            """,
            (user_id, customer_name, phone, address, total)
        )

        db.commit()

        session.pop("cart", None)

        return "🎉 Order Placed Successfully!"

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

    return render_template(
        "dashboard.html",
        orders=orders
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

    return render_template("index.html", foods=foods)


if __name__ == "__main__":
    app.run(debug=True)