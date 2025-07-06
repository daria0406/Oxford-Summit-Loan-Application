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
    average_processing_time: float
    average_requested_amount: float
    ratio_costs_to_income: float
    analysis_summary: str
    