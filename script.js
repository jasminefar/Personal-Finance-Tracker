document.getElementById('transaction-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const type = document.getElementById('type').value;
    const category = document.getElementById('category').value;
    const amount = document.getElementById('amount').value;
    const description = document.getElementById('description').value;
    
    const data = { type, category, amount, description };
    
    fetch('/add_transaction', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        alert('Transaction added successfully');
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

document.getElementById('generate-report').addEventListener('click', function() {
    fetch('/report')
    .then(response => response.json())
    .then(data => {
        const reportDiv = document.getElementById('report');
        reportDiv.innerHTML = `
            <p>Total Income: ${data.total_income}</p>
            <p>Total Expense: ${data.total_expense}</p>
            <p>Balance: ${data.balance}</p>
        `;
    });
});