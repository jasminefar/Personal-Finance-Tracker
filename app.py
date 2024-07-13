<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Finance Tracker</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="content">
        <h1>Personal Finance Tracker</h1>
        <div class="container">
            <h2>Add Transaction</h2>
            <form id="transaction-form">
                <label for="type">Type:</label>
                <select id="type" name="type">
                    <option value="Income">Income</option>
                    <option value="Expense">Expense</option>
                </select>
                <label for="category">Category:</label>
                <input type="text" id="category" name="category" placeholder="e.g., Salary, Food" required>
                <label for="amount">Amount:</label>
                <input type="number" id="amount" name="amount" placeholder="e.g., 1000" required>
                <label for="description">Description:</label>
                <input type="text" id="description" name="description" placeholder="e.g., January Salary">
                <button type="submit">Add Transaction</button>
            </form>
        </div>
        <button id="generate-report">Generate Report</button>
        <div id="report" class="container">
            <h2>Report</h2>
            <div id="report-content"></div>
        </div>
    </div>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
