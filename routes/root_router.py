from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def root():
    return {"mensagem":"Hello World!!!"}