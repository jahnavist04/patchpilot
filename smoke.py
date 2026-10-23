from app import config
from app.agent.llm import METRICS, chat
from tavily import TavilyClient

model = config.MODELS["classify"]
assert model, "Set MODEL_NANO in .env"
print("LLM:", chat("classify", [{"role": "user", "content": "Say hi in 5 words."}], model=model))
print("Metrics:", METRICS[-1])

tv = TavilyClient(api_key=config.TAVILY_API_KEY)
for r in tv.search("requests library CVE fixed version advisory", max_results=3)["results"]:
    print("-", r["title"], r["url"])
