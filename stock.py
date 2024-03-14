import requests
from datetime import datetime

class Stock:
    def __init__(self, symbol, quantity, purchase_price):
        self.symbol = symbol
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.last_updated = None
        self.current_price = None

    def fetch_current_price(self):
        # Fetch real-time data from Alpha Vantage API
        api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={self.symbol}&apikey={api_key}'
        try:
            response = requests.get(url)
            data = response.json()
            if 'Global Quote' in data:
                self.current_price = float(data['Global Quote']['05. price'])
                self.last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                raise ValueError("Invalid response from API")
        except Exception as e:
            print(f"Failed to fetch data for {self.symbol}: {e}")

    def current_value(self):
        if not self.current_price:
            self.fetch_current_price()
        if self.current_price:
            return self.current_price * self.quantity
        else:
            return None

    def __str__(self):
        return f"Symbol: {self.symbol}, Quantity: {self.quantity}, Purchase Price: {self.purchase_price}, Current Price: {self.current_price}, Last Updated: {self.last_updated}"

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, symbol, quantity, purchase_price):
        stock = Stock(symbol, quantity, purchase_price)
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        self.stocks = [stock for stock in self.stocks if stock.symbol != symbol]

    def portfolio_value(self):
        total_value = 0
        for stock in self.stocks:
            value = stock.current_value()
            if value:
                total_value += value
        return total_value

    def display_portfolio(self):
        print("Stock Portfolio:")
        for stock in self.stocks:
            print(stock)

# Example usage
def main():
    portfolio = Portfolio()

    portfolio.add_stock("AAPL", 10, 120)
    portfolio.add_stock("GOOG", 5, 2000)
    portfolio.add_stock("MSFT", 8, 150)

    print("Portfolio Value:", portfolio.portfolio_value())
    portfolio.display_portfolio()

    # Removing a stock
    portfolio.remove_stock("AAPL")

    print("Portfolio Value:", portfolio.portfolio_value())
    portfolio.display_portfolio()

if __name__ == "__main__":
    main()