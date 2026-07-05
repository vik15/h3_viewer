from fastapi import APIRouter
import h3

router = APIRouter(prefix="/property")



@router.get("/get_resolution")
def get_resolution(cell):
    return h3.get_resolution(cell)



@router.get("/get_base_cell_number")
def get_base_cell_number(cell):
    return h3.get_base_cell_number(cell)



@router.get("/get_all_pentagons")
def get_all_pentagons(res=9):
    return h3.get_pentagons(res)