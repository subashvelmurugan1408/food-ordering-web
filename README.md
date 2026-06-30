# 🍔 Online Food Delivery Website

A full-stack **Online Food Delivery Website** developed using **Python Flask**, **MySQL**, **HTML**, **CSS**, and **JavaScript**. This project allows users to browse food items, register, log in, add items to a cart, place orders, and provides an admin panel to manage food items.

---

## 🚀 Features

### 👤 User Features

* User Registration
* User Login & Logout
* Browse Food Menu
* Add Food to Cart
* Shopping Cart
* Checkout
* Place Orders
* User Dashboard
* View Order History

### 👨‍💼 Admin Features

* Admin Dashboard
* Add Food Items
* Edit Food Items
* Delete Food Items
* View Customer Orders

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* MySQL

### Other Tools

* VS Code
* MySQL Workbench
* Git
* GitHub

---

## 📂 Project Structure

```text
FoodDelivery/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       ├── logo.png
│       ├── burger.jpg
│       ├── pizza.jpg
│       ├── biryani.jpg
│       ├── fries.jpg
│       ├── pasta.jpg
│       └── sandwich.jpg
│
└── templates/
    ├── index.html
    ├── register.html
    ├── login.html
    ├── cart.html
    ├── checkout.html
    ├── dashboard.html
    ├── admin.html
    ├── add_food.html
    ├── edit_food.html
    └── orders.html
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/online-food-delivery.git
```

### Move into the Project

```bash
cd online-food-delivery
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure MySQL

Create a database named:

```sql
CREATE DATABASE food_delivery;
```

Import the required tables into the database.

### Update Database Credentials

Edit `app.py`:

```python
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="YOUR_PASSWORD",
    database="food_delivery"
)
```

### Run the Project

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🗄️ Database Tables

* users
* food
* orders

---

## 📸 Screens

* Home Page
* Registration Page
* Login Page
* Food Menu
* Shopping Cart
* Checkout
* User Dashboard
* Admin Dashboard
* Orders Page

---

## 📌 Future Enhancements

* Secure password hashing
* Food search
* Food categories
* Image upload from admin panel
* Quantity update in cart
* Payment gateway integration
* Email notifications
* Responsive mobile design
* Admin authentication
* Cloud deployment

---

## 📚 Learning Outcomes

This project helped in understanding:

* Flask Routing
* HTML Forms
* CRUD Operations
* MySQL Integration
* User Authentication
* Session Management
* Shopping Cart Logic
* Order Processing
* Admin Panel Development
* Full-Stack Web Development

---

## 👨‍💻 Author

**Subash V**

* B.E. Computer Science and Engineering
* RVS Technical Campus, Coimbatore

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!
