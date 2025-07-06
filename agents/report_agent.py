from agents import Agent, function_tool, RunContextWrapper

@function_tool()
def synthesize_report(wrapper: RunContextWrapper[dict]) -> str:
    context = wrapper.context
    return f"""📋 Loan Application System Summary
Dear {context.get('to', 'Daria Zahaleanu')},
Recommendation: {context.get('recommendation', 'No recommendation')}
Fraud Result: {context.get('fraud_result')}
SLA Result: {context.get('sla_result')}
Interest Rate Result: {context.get('interest_rate_result')}

Regards,
Team 5 - Loan Application Agent
"""

report_agent = Agent(
    name="ReportAgent",
    instructions="Generate a professional summary report for the loan application decision. Address it to Daria Zahaleanu",
    model="gpt-4o-mini",
    tools=[synthesize_report],
    output_type=str
)