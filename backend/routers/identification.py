from fastapi import APIRouter
import h3

router = APIRouter(prefix="/identify")


@router.get("/is_pentagon")
def is_pentagon(cell):
    return h3.is_pentagon(cell)
