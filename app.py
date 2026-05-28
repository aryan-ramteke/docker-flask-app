from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        return "Hello World! Connected to MySQL successfully."

    except Exception as e:
        return f"Database connection failed: {str(e)}"


app.run(host="0.0.0.0", port=5000)
