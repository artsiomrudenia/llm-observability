from fastapi import FastAPI

app = FastAPI(title="llm-observability", version="0.1.0")


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.get("/info")
def info() -> dict:
    return {
        "project": "llm-observability",
        "description": "Metrics and tracing gateway for LLM applications",
        "domain": "observability",
    }
