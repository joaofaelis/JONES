from fastapi import FastAPI
from src.router.routers import API
app = FastAPI(
    title="Login/Register",
    description="API desenvolvida para registros e logins",
    version="0.0.1"
)

app.include_router(API)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)