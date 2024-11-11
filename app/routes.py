from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    mock_user = {'username': 'Pandozz'}

    mock_expenses = [
        {'date': '2024-11-11 14:30',
         'amount': 6.50,
         'category': 'Food',
         'description': 'Icecream'},
        {'date': '2024-11-12 08:45',
         'amount': 5.00,
         'category': 'Transportation',
         'description': 'Bus fare'},
        {'date': '2024-11-13 12:15',
         'amount': 20.00,
         'category': 'Entertainment',
         'description': 'Movie ticket'},
        {'date': '2024-11-14 18:00',
         'amount': 15.99,
         'category': 'Shopping',
         'description': 'Gift for friend'},
        {'date': '2024-11-15 10:00',
         'amount': 20.00,
         'category': 'Food',
         'description': 'Breakfast'}
    ]

    return render_template(
        'index.html',
        title='Home',
        user=mock_user,
        expenses=mock_expenses
    )
