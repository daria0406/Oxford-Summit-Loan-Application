from agents import function_tool, RunContextWrapper
from data_model import TrendAnalysisResult

@function_tool(strict_mode=False)
def synthesize_summary(wrapper: RunContextWrapper[TrendAnalysisResult], config=None) -> dict:
    r = wrapper.context
    return {
        "application_id": r.application_id,
        "sla_result": r.sla_result,
        "fraud_result": r.fraud_result,
        "affordability_result": r.affordability_result,
        "affordability_level": r.affordability_level,
        "recommendation": r.recommendation,
        "explanation": r.explanation,
        "timestamp": r.timestamp,
        "final_decision": r.final_decision,
        "explanation_sources": getattr(r, "explanation_sources", {}),
        "summary_text": f"""✉️ **Loan Decision Summary**
- Application ID: {r.application_id}
- Final Decision: {r.final_decision}
- SLA Result: {r.sla_result}
- Fraud Result: {r.fraud_result}
- Affordability: {r.affordability_result} ({r.affordability_level})
- Recommendation: {r.recommendation}
- Explanation: {r.explanation}
- Timestamp: {r.timestamp}"""
    }
