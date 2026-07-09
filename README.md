# 🍔 FoodExpress - Online Food Ordering Website

A modern **Full Stack Food Ordering Website** built using **Python Flask**, **MySQL**, **AWS RDS**, and **HTML/CSS/JavaScript**. Users can browse food items, search meals, manage their cart, place orders, and view their order history through a responsive web interface.

---

## 🚀 Live Demo

> **Live URL:** *(https://food-ordering-web-1.onrender.com)*

---

## 📸 Screenshots

### 🏠 Home Page
(Add Screenshot)

### 🛒 Shopping Cart
(Add Screenshot)

### 💳 Checkout
(Add Screenshot)

### 📦 User Dashboard
(Add Screenshot)

### ✅ Order Success Page
(Add Screenshot)

---

# ✨ Features

## 👤 User Authentication
- User Registration
- User Login
- Logout
- Session Management

## 🍽 Food Menu
- Dynamic food cards
- Food images
- Search functionality
- Responsive layout

## 🛒 Shopping Cart
- Add to cart
- Remove items
- Increase quantity
- Decrease quantity
- Automatic total calculation

## 💳 Checkout
- Customer details
- Delivery address
- Order summary
- Order confirmation page

## 📦 Dashboard
- View previous orders
- Order history

## ☁ Deployment
- AWS RDS MySQL Database
- Render Deployment
- Environment Variables
- Gunicorn

---

# 🛠 Technologies Used

## Backend
- Python
- Flask

## Frontend
- HTML5
- CSS3
- JavaScript

## Database
- MySQL
- AWS RDS

## Deployment
- Render
- GitHub
- Gunicorn

---

# 📂 Project Structure

```
food-ordering-web/

│

├── static/

│   ├── css/

│   │      style.css

│   │      cart.css

│   │      checkout.css

│   │      order_success.css

│   │

│   ├── images/

│   └── js/

│

├── templates/

│      index.html

│      login.html

│      register.html

│      cart.html

│      checkout.html

│      dashboard.html

│      order_success.html

│

├── app.py

├── requirements.txt

├── README.md

└── .gitignore
```

---

# 🗄 Database

## Users

```
id
fullname
email
phone
password
```

## Food

```
id
food_name
price
image
```

## Orders

```
id
user_id
customer_name
phone
address
total_amount
order_date
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/subashvelmurugan1408/food-ordering-web.git
```

Go to the project folder

```bash
cd food-ordering-web
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run the Flask App

```bash
python app.py
```

---

# 🌐 Environment Variables

Create the following environment variables (or configure them in Render):

```env
DB_HOST=your_rds_endpoint
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database_name
DB_PORT=3306
SECRET_KEY=your_secret_key
```

---

# 🚀 Deployment

This project is deployed using:

- Render
- AWS RDS MySQL

Deployment Steps

1. Push code to GitHub
2. Create a Render Web Service
3. Connect GitHub Repository
4. Add Environment Variables
5. Deploy

---

# 📚 What I Learned

- Flask Web Development
- Authentication & Sessions
- MySQL Database Integration
- AWS RDS Configuration
- Cloud Deployment using Render
- Environment Variables
- Git & GitHub Workflow
- Responsive Web Design
- Debugging Deployment Errors
- Shopping Cart Logic

---

# 🔮 Future Improvements

- Admin Panel
- Food Categories
- Payment Gateway Integration
- Order Tracking
- Food Ratings & Reviews
- Coupon System
- Email Notifications
- Image Upload for Admin
- Online Payments (Stripe/Razorpay)

---

# 👨‍💻 Author

**Subash V**

🎓 B.E Computer Science and Engineering

📍 Tamil Nadu, India

### GitHub

https://github.com/subashvelmurugan1408

### LinkedIn

(Add your LinkedIn URL)

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.

---

## 📄 License

This project is developed for educational and portfolio purposes.
