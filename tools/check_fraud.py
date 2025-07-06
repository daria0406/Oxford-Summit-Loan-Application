from agents import function_tool, RunContextWrapper
from data_model import LoanApplicationJourney

@function_tool()
def check_fraud(wrapper: RunContextWrapper[LoanApplicationJourney], config=None) -> dict:
    ctx = wrapper.context
    rules = config.get_fraud_rules() if config else {}

    flagged = bool(ctx.flagged_for_fraud)

    return {
        "flagged": flagged,
        "label": "⚠️ Fraud flag triggered" if flagged else "No fraud indicators detected",
        "risk_score": 1.0 if flagged else 0.0,
        "triggered_rules": ["hard_flag"] if flagged else [],
        "explanation": "Manually flagged application" if flagged else "No indicators present"
    }
