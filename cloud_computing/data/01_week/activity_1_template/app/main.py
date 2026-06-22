from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.files.router import router as file_router

app = FastAPI()

@app.get("/healthcheck")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

app.include_router(auth_router)
app.include_router(file_router, prefix="/files")
