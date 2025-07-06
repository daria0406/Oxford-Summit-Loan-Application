from agents import function_tool, RunContextWrapper
from data_model import LoanApplicationJourney
from utils.config_loader import ConfigLoader
import yfinance as yf
import json
import os
    
@function_tool()
def check_acceptability_threshold(rate=None):
    """
    Checks the interest rate against thresholds in config.json.
    Returns a dict with level and label.
    """
    # get the interest rate
    rate = get_interest_rate()['rate']

    # Runs the check against the thresholds defined in config.json
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    thresholds = config.get("interest_rate_thresholds", [])
    if rate is None:
        return {"error": "No rate provided."}
    for threshold in thresholds:
        if rate <= threshold["max_rate"]:
            return {"level": threshold["level"], "label": threshold["label"]}
    return {"level": "reject", "label": "Unacceptable"}

@function_tool()
def get_interest_rate(wrapper=None, config=None):
    """
    Fetch the latest interest rate (^TNX) from Yahoo Finance.
    Returns a dict with rate, date, and source.
    """
    ticker = "^TNX"
    data = yf.Ticker(ticker)
    hist = data.history(period="5d")
    if not hist.empty:
        latest_rate = hist['Close'][-1]
        latest_date = str(hist.index[-1].date())
        return {
            'rate': float(latest_rate),
            'date': latest_date,
            'source': 'Yahoo Finance (^TNX)'
        }
    else:
        return {
            'error': 'No data found for interest rate ticker (^TNX) on Yahoo Finance.'
        }