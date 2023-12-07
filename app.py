from flask import Flask, render_template, request, redirect, url_for, session
from helper import *

app = Flask(__name__)

@app.route('/')
def index():
    top_gainers = top_10_gainers()
    return render_template('index.html', top_gainers=top_gainers)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ticker = request.form['ticker']
        stock_data = search_stock(ticker)
        return render_template('result.html', stock_data=stock_data)

    return render_template('404.html'), 404

@app.route('/user')
def user():
    user_interests = session.get('interests', [])
    return render_template('user.html', user_interests=user_interests)

@app.route('/add_interest', methods=['POST'])
def add_interest():
    ticker = request.form['ticker']
    user_interests = session.get('interests', [])

    # Check if the stock is not already in the interest list
    if ticker not in user_interests:
        user_interests.append(ticker)
        session['interests'] = user_interests

    return redirect(url_for('search'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
