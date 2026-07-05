from fastapi import APIRouter
import h3


router = APIRouter(prefix="/index")



@router.get("/get_str_to_int")
def get_str_to_int(cell, rou):
    return h3.str_to_int(cell)


@router.get("/get_int_to_str")
def get_int_to_str(cell):
    return h3.int_to_str(cell)
