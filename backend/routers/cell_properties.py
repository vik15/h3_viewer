from fastapi import APIRouter
import h3

router = APIRouter(prefix="/property")



@router.get("/get_res0_cells")
def get_resolution_0_cells():
    return h3.get_res0_cells()



@router.get("/get_all_pentagons")
def get_all_pentagons(res: int =9):
    return h3.get_pentagons(res)



@router.get("/get_num_cells")
def get_num_cells(res: int = 9):
    return h3.get_num_cells(res)



@router.get("/get_resolution")
def get_resolution(cell):
    return h3.get_resolution(cell)



@router.get("/get_base_cell_number")
def get_base_cell_number(cell):
    return h3.get_base_cell_number(cell)



@router.get("/get_index_digit")
def get_index_digit(cell,res: int=9):
    return h3.get_index_digit(cell,res)



@router.get("/construct_cell")
def construct_cell(base_cell_number,*digits,res):
    return h3.construct_cell(base_cell_number,*digits,res)



@router.get("/deconstruct_cell")
def deconstruct_cell(cell):
    return h3.deconstruct_cell(cell)