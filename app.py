from flask import Flask, render_template, request, redirect, url_for, session
from helper import *

app = Flask(__name__)
app.secret_key = '0000'  

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/top_gainers')
def top_gainers():
    gainers_data = top_10_gainers()
    return render_template('top_gainers.html', top_gainers=gainers_data)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ticker = request.form['ticker']
        stock_data = get_stock_info(ticker)
        return render_template('result.html', stock_data=stock_data, ticker=ticker)
    return render_template('search.html')


@app.route('/portfolio')
def portfolio():
    portfolio_stocks = session.get('portfolio', [])
    portfolio_data = [get_stock_info(stock) for stock in portfolio_stocks]
    return render_template('portfolio.html', portfolio_data=portfolio_data)


@app.route('/add_to_portfolio', methods=['POST'])
def add_to_portfolio():
    ticker = request.form['ticker']
    if ticker:
        portfolio = session.get('portfolio', [])
        if ticker not in portfolio:
            portfolio.append(ticker)
            session['portfolio'] = portfolio

    return redirect(url_for('portfolio'))


@app.route('/remove_from_portfolio/<ticker>', methods=['POST'])
def remove_from_portfolio(ticker):
    portfolio = session.get('portfolio', [])

    # Remove the ticker if it's in the portfolio
    if ticker in portfolio:
        portfolio.remove(ticker)
        session['portfolio'] = portfolio
        session.modified = True

    return redirect(url_for('portfolio'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
