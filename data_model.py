from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class LoanApplicationJourney:
    application_id: str
    submitted_time: str
    reviewed_time: str
    approved_time: Optional[str]
    rejected_time: Optional[str]
    processing_steps: Dict[str, int]
    flagged_for_fraud: bool
    monthly_income: Optional[float] = None
    monthly_costs: Optional[float] = None
    requested_amount: Optional[float] = None
    monthly_debt: Optional[float] = 0.0

@dataclass
class TrendAnalysisResult:
    application_id: str
    sla_result: str
    fraud_result: str
    recommendation: str
    explanation: str
    timestamp: str
    affordability_result: Optional[str] = None
    affordability_level: Optional[str] = None
    final_decision: Optional[str] = None