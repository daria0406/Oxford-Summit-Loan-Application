# Deterministic Agent Workflor for Financial Service - Loan Application Processing

This repository demonstrates a full loan application decision process using an **agent orchestration pipeline** powered by OpenAI Agents SDK and custom tools.

## Overview

- **Main.ipynb** walks through the orchestration of multiple agents to analyze a loan application.
- The pipeline checks for fraud, SLA compliance, and interest rate acceptability, then synthesizes a final recommendation.
- The final report can be sent via email using a Zapier webhook integration.

## Features

- **Agent-based orchestration**: Modular agents for fraud detection, SLA, interest rate, and recommendations.
- **Configurable pipeline**: Easily adjust thresholds and logic via config files or agent instructions.
- **Automated reporting**: Generates a summary report and sends it via email using Zapier.

## How to Run

1. **Clone the repository** and install dependencies:
    ```sh
    git clone <repo-url>
    cd Oxford-Summit-Loan-Application
    pip install -r requirements.txt
    ```

2. **Set up environment variables**:
    - Create a `.env` file with your OpenAI API key and your Zapier webhook URL:
      ```
      OPENAI_API_KEY=your-openai-key
      MCP_SERVER_URL_SSE=https://hooks.zapier.com/hooks/catch/your_zapier_id/your_path/
      ```

3. **Configure Zapier**:
    - Create a Zap with a "Catch Hook" trigger and a Gmail (or Email) action.
    - Map the fields as described in the notebook and previous instructions.

4. **Open `Main.ipynb` in VS Code or Jupyter** and run the cells step by step.

## Sending Email Reports

- The notebook uses a `ZapierChannel` class to send the final report to your Zapier webhook.
- The payload includes the report message and metadata (subject, recipient).
- Ensure your Zapier action maps `metadata.to`, `metadata.subject`, and `message` or `metadata.body` to the correct email fields.

## Key Files

- `Main.ipynb` — The main orchestration notebook.
- `agents/` — Contains agent definitions and tools.
- `mcp/zapier_channel.py` — Helper for sending data to Zapier webhooks.
- `data_model.py` — Data structures for the loan application journey.

## Example Usage: How the Pipeline Runs

Here’s a minimal example of how to use the pipeline in code:

```python
# 1. Create a sample application
test_app = LoanApplicationJourney(
    application_id="APP-EXAMPLE-001",
    submitted_time="2025-06-01T09:00:00",
    reviewed_time="2025-06-01T09:30:00",
    approved_time="2025-06-01T10:00:00",
    rejected_time=None,
    processing_steps={"KYC": 72, "CreditCheck": 50, "FinalApproval": 35},
    flagged_for_fraud=False,
    monthly_income=50000,
    monthly_costs=1000,
    requested_amount=25000,
    monthly_debt=400
)

# 2. Run each agent
fraud_result = fraud_agent.tools[0](RunContextWrapper(test_app))
sla_result = sla_agent.tools[0](RunContextWrapper(test_app))
interest_rate_result = interest_rate_agent.tools[0](RunContextWrapper(test_app))

# 3. Get recommendation
recommendation = get_recommendation(fraud_result, sla_result, interest_rate_result)

# 4. Prepare context and generate report
final_context = {
    "recommendation": getattr(recommendation, 'final_output', recommendation),
    "fraud_result": fraud_result,
    "sla_result": sla_result,
    "interest_rate_result": interest_rate_result
}
report_result = report_agent.tools[0](RunContextWrapper(final_context))

# 5. Print results
print("Fraud Result:", fraud_result)
print("SLA Result:", sla_result)
print("Interest Rate Result:", interest_rate_result)
print("Recommendation:", recommendation)
print("System Summary Report:\n", report_result)
```

**Sample Output:**
```
Fraud Result: {'flagged': False, 'reason': 'No fraud indicators detected.'}
SLA Result: {'violated': False, 'details': 'All steps within SLA.'}
Interest Rate Result: {'rate': 0.045, 'date': '2025-07-06', 'source': 'Yahoo Finance (^TNX)'}
Recommendation: Approve the loan application. No fraud or SLA violations detected. Interest rate is reasonable.
System Summary Report:
📋 Loan Application System Summary

Recommendation: Approve the loan application. No fraud or SLA violations detected. Interest rate is reasonable.
Fraud Result: {'flagged': False, 'reason': 'No fraud indicators detected.'}
SLA Result: {'violated': False, 'details': 'All steps within SLA.'}
Interest Rate Result: {'rate': 0.045, 'date': '2025-07-06', 'source': 'Yahoo Finance (^TNX)'}

Regards,
AI Loan System
```
## 5. Further Work

## 6. Authors - Team 5, Full Code

- Daria Zahaleanu
- Cesare Aloisi
- Luca Di Carlo
- Steven Kok
- Jothibasu Ramachandran
- Rosie 