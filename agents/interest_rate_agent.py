from agents import Agent, function_tool
from tools.check_acceptability_threshold import check_acceptability_threshold

interest_rate_agent = Agent(
    name="InterestRateAgent",
    instructions="Fetch the current interest rate using yfinance.",
    tools=[check_acceptability_threshold],
    model="gpt-3.5-turbo",
    output_type=dict
)
