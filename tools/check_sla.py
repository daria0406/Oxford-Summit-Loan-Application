from agents import function_tool, RunContextWrapper
from data_model import LoanApplicationJourney
from utils.config_loader import ConfigLoader

@function_tool()
def check_sla(wrapper: RunContextWrapper[LoanApplicationJourney], config=None) -> dict:
    journey = wrapper.context
    thresholds = config.get_sla_thresholds() if config else {}

    violations = []
    for step, duration in journey.processing_steps.items():
        limit = thresholds.get(step, 60)  # fallback SLA
        if duration > limit:
            violations.append(step)

    return {
        "violated": bool(violations),
        "label": f"SLA violations in: {', '.join(violations)}" if violations else "All steps within SLA.",
        "violated_steps": violations,
        "explanation": "Steps exceeded configured SLA limits." if violations else "All steps met SLA thresholds."
    }