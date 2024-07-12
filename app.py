from flask import Flask, request, jsonify, render_template
import csv
import pandas as pd
from datetime import datetime

app = Flask(__name__)

FILENAME = "finance_data.csv"

# Initialize the CSV file if it doesn't exist
def init_file():
    try:
        with open(FILENAME, mode='r') as file:
            pass
    except FileNotFoundError:
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type", "Category", "Amount", "Description"])

init_file()

# Route to add a transaction
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.json
    transaction_type = data['type']
    category = data['category']
    amount = data['amount']
    description = data.get('description', "")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, transaction_type, category, amount, description])
    
    return jsonify({"message": "Transaction added successfully"}), 201

# Route to generate a report
@app.route('/report', methods=['GET'])
def report():
    df = pd.read_csv(FILENAME)
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    balance = total_income - total_expense
    
    report_data = {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance
    }
    return jsonify(report_data)

# Route to render the homepage
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)