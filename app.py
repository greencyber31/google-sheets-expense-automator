import gspread
from oauth2client.service_account import ServiceAccountCredentials
from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from datetime import datetime

app = Flask(__name__)

# 1. Setup Google Sheets Connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
# Ensure your credentials.json is in the Expense_Tracker_2 folder!
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# 2. Open the Sheet
# Replace 'Your Sheet Name' with the actual name of your Google Sheet
sheet = client.open("Expense_Tracker_2").sheet1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_expense():
    try:
        # Get data from the form
        data = request.json
        
        # Prepare the row for Google Sheets
        # Order: Date, Category, Name, Amount
        new_row = [
            data.get('date'),
            data.get('category'),
            data.get('item_name'),
            data.get('amount')
        ]
        
        sheet.append_row(new_row)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error adding expense: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
