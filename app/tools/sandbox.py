from app.contracts import SandboxResult


def verify(repo_path: str, patch: str) -> SandboxResult:
    # TODO: apply patch on a copy, docker build (network on), run tests (network off), re-scan
    return SandboxResult(tests_passed=True, tests_total=18, tests_failed=0,
                         finding_still_present=False, logs="mock", duration_s=0.0)
