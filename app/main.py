from fastapi import FastAPI

app = FastAPI(title="Secure Notes API")


@app.get("/health")
def health_check():
    return {"status": "ok"}

