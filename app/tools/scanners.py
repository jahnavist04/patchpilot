from app.contracts import Finding


def scan(repo_path: str) -> list[Finding]:
    # TODO: run pip-audit, bandit, detect-secrets and map to Finding
    return [Finding(id="f-001", type="sql_injection", file="app/db.py",
                    line=42, severity="high", detail="Query built with string formatting")]
