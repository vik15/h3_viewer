from fastapi import APIRouter
import h3

router = APIRouter(prefix="/hierarchy")



@router.get("/get_parent_of_cell")
def get_parent_of_cell(cell):
    return h3.cell_to_parent(cell)



@router.get("/get_children_of_cell")
def get_children_of_cell(cell):
    return h3.cell_to_children(cell)
