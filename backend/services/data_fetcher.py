def get_stock_data(symbol: str):
    """
    Placeholder stock data fetcher.
    Later we’ll connect this to Yahoo Finance or Alpha Vantage API.
    """
    example_data = {
        "price": 1234.56,
        "change": "+2.15%",
        "sector": "Technology",
        "market_cap": "1.2T",
        "pe_ratio": 25.6,
        "recommendation": "Buy"
    }
    return example_data


def get_mutualfund_data(name: str):
    """
    Placeholder mutual fund data fetcher.
    Later this will fetch data from AMFI, Value Research, or Groww APIs.
    """
    example_data = {
        "NAV": 102.34,
        "1Y_return": "12.5%",
        "category": "Equity - Large Cap",
        "fund_manager": "HDFC AMC",
        "expense_ratio": "1.1%",
        "recommendation": "Hold"
    }
    return example_data
