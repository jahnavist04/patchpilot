from tavily import TavilyClient
from app import config
from app.contracts import Finding

_tv = TavilyClient(api_key=config.TAVILY_API_KEY)


def research(finding: Finding) -> dict:
    if finding.type == "dependency":
        query = f"{finding.detail} CVE advisory fixed version"
    elif finding.type == "sql_injection":
        query = "python parameterized queries fix SQL injection string formatting"
    else:
        query = "python remove hardcoded secrets use environment variables best practice"

    results = _tv.search(query, max_results=3).get("results", [])
    summary = "\n".join(f"- {r['title']}: {r['content'][:300]}" for r in results)
    return {"summary": summary, "urls": [r["url"] for r in results]}
