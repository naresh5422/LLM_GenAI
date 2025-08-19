from fastapi import APIRouter
router = APIRouter()
@router.get("/health")
async def health():
    """
    Health check endpoint.
    Returns a simple message indicating the service is running.
    """
    return {"status": "ok", "message": "Service is running"}