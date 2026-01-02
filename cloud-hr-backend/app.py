from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

# 1️⃣ Create app
app = Flask(__name__)
CORS(app)

# 2️⃣ Database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="cloud_hr"
)
cursor = db.cursor(dictionary=True)

# 3️⃣ Home route (test)
@app.route("/")
def home():
    return "Cloud HR Backend Running Successfully"

# 4️⃣ Login API
@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    cursor.execute(
        "SELECT * FROM employees WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    if user:
        return jsonify({
            "status": "success",
            "user": {
                "id": user["id"],
                "name": user["full_name"],
                "email": user["email"],
                "role": user["role"]
            }
        })
    else:
        return jsonify({"error": "Invalid email or password"}), 401

# 5️⃣ Employees API
@app.route("/api/employees", methods=["GET"])
def get_employees():
    cursor.execute("SELECT * FROM employees")
    return jsonify(cursor.fetchall())

# 🔽🔽🔽 ADD DASHBOARD API HERE 🔽🔽🔽
@app.route("/api/dashboard", methods=["GET"])
def dashboard_data():
    cursor.execute("SELECT COUNT(*) AS total FROM employees")
    total = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS active FROM employees WHERE status='active'")
    active = cursor.fetchone()["active"]

    cursor.execute("SELECT COUNT(*) AS admins FROM employees WHERE role='admin'")
    admins = cursor.fetchone()["admins"]

    cursor.execute("""
        SELECT id, full_name, email, role, created_at
        FROM employees
        ORDER BY created_at DESC
        LIMIT 5
    """)
    latest = cursor.fetchall()

    return jsonify({
        "total_employees": total,
        "active_employees": active,
        "admins": admins,
        "latest_employees": latest
    })

# 6️⃣ Start server (ALWAYS LAST)
if __name__ == "__main__":
    app.run(debug=True)
