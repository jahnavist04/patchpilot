from typing import Literal, Optional
from pydantic import BaseModel

FindingType = Literal["dependency", "sql_injection", "hardcoded_secret"]
Severity = Literal["low", "medium", "high", "critical"]


class Finding(BaseModel):
    id: str
    type: FindingType
    file: str
    line: int
    severity: Severity
    detail: str


class SandboxResult(BaseModel):
    tests_passed: bool
    tests_total: int
    tests_failed: int
    finding_still_present: bool
    logs: str
    duration_s: float


class CallMetric(BaseModel):
    model: str
    purpose: str
    prompt_tokens: int
    completion_tokens: int
    latency_s: float


class Attempt(BaseModel):
    number: int
    diff: str
    result: SandboxResult


class FindingOutcome(BaseModel):
    finding: Finding
    status: Literal["fixed", "needs_human_review"]
    attempts: list[Attempt]
    explanation: str = ""
    advisory_urls: list[str] = []


class RunReport(BaseModel):
    run_id: str
    repo: str
    outcomes: list[FindingOutcome]
    metrics: list[CallMetric] = []
    scan_before: list[Finding] = []
    scan_after: list[Finding] = []
    error: Optional[str] = None
