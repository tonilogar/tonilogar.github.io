from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.post("/login")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.post("/logout")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/introspect")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
