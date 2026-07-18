from fastapi import FastAPI

app = FastAPI(
    title="Solar Plant Monitoring System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Solar Plant Monitoring Backend Running"
    }