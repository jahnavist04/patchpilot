import time
from openai import OpenAI
from app import config
from app.contracts import CallMetric

_client = OpenAI(base_url=config.NEBIUS_BASE_URL, api_key=config.NEBIUS_API_KEY)
METRICS: list[CallMetric] = []


def chat(purpose: str, messages: list[dict], model: str | None = None, **kwargs) -> str:
    model = model or config.MODELS[purpose]
    start = time.perf_counter()
    resp = _client.chat.completions.create(model=model, messages=messages, **kwargs)
    latency = time.perf_counter() - start
    u = resp.usage
    METRICS.append(CallMetric(
        model=model,
        purpose=purpose,
        prompt_tokens=getattr(u, "prompt_tokens", 0),
        completion_tokens=getattr(u, "completion_tokens", 0),
        latency_s=round(latency, 3),
    ))
    return resp.choices[0].message.content or ""
