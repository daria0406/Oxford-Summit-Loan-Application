from utils.config_loader import ConfigLoader


def explain_decision(sla_result: dict, fraud_result: dict, affordability_result: dict = None, config=None) -> dict:
    templates = config.get_explanation_templates() if config else ConfigLoader().get_explanation_templates()
    messages = []

    if affordability_result and affordability_result.get("level") == "reject":
        messages.append(templates.get("low_affordability", affordability_result.get("label", "")))

    if fraud_result.get("flagged"):
        messages.append(templates.get("fraud_flagged", fraud_result.get("label", "")))

    if sla_result.get("violated"):
        messages.append(templates.get("sla_violation", sla_result.get("label", "")))

    if not messages:
        messages.append(templates.get("clean", "No issues detected."))

    return {
        "explanation": " ".join(messages),
        "sources": {
            "affordability": affordability_result.get("label") if affordability_result else "",
            "fraud": fraud_result.get("label"),
            "sla": sla_result.get("label")
        }
    }