from agents import Agent, function_tool, RunContextWrapper

@function_tool()
def synthesize_report(wrapper: RunContextWrapper[dict]) -> str:
    context = wrapper.context
    return f"""📋 Loan Application System Summary
    
This report summarizes the analysis of the loan application system.
Average_processing_time: {context.get('average_processing_time', 'N/A')}
Average Requested Amount: {context.get('average_requested_amount', 'N/A')}
Ratio of Costs to Income: {context.get('ratio_costs_to_income', 'N/A')}
Analysis Summary: {context.get('analysis_summary', 'N/A')}

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