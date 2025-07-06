from agents import Agent
from data_model import LoanApplicationJourney
from tools.check_fraud import check_fraud

fraud_agent = Agent[LoanApplicationJourney](
    name="FraudDetectionAgent",
    instructions="You are a compliance analyst. Use the fraud detection tool "
        "to determine if the loan application has fraud indicators. "
        "Do not rely on your own judgment — always call the tool.",
    model="gpt-4-0613",
    tools=[check_fraud],
    output_type=str
)