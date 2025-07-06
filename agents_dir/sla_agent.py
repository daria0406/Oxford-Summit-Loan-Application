from agents import Agent
from data_model import LoanApplicationJourney
from tools.check_sla import check_sla

sla_agent = Agent[LoanApplicationJourney](
    name="SLAComplianceAgent",
    instructions="Use the tool to evaluate SLA compliance.",
    model="gpt-4-0613",
    tools=[check_sla],
    output_type=str
)