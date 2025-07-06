from agents import function_tool, RunContextWrapper
from data_model import LoanApplicationJourney
from utils.config_loader import ConfigLoader

@function_tool()
def check_affordability(wrapper: RunContextWrapper[LoanApplicationJourney], config=None) -> dict:
    journey = wrapper.context
    income = journey.monthly_income
    requested = journey.requested_amount
    debt = journey.monthly_debt or 0.0
    costs = journey.monthly_costs or 0.0

    if income is None or requested is None:
        return {"label": "Affordability data missing", "level": "unknown"}

    ratio = (requested + debt * 12) / (income * 12)
    thresholds = config.get_affordability_thresholds() if config else ConfigLoader().get_affordability_thresholds()

    for rule in thresholds:
        if ratio <= rule["max_ratio"]:
            return {
                "label": rule["label"],
                "level": rule["level"],
                "ratio": round(ratio, 3),
                "threshold_matched": rule["max_ratio"],
                "explanation": f"Ratio {ratio:.2f} matched affordability threshold {rule['max_ratio']}"
            }

    return {
        "label": "❌ Affordability result unavailable",
        "level": "unknown",
        "ratio": ratio,
        "threshold_matched": None,
        "explanation": "No threshold matched for given ratio."
    }
