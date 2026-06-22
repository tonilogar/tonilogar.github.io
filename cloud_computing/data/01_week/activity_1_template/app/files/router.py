from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.post("")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/{id}")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.post("/{id}")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.delete("/{id}")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

@router.post("/merge")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
