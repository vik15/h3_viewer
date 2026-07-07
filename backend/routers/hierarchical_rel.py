from fastapi import APIRouter
import h3

router = APIRouter(prefix="/hierarchy")



@router.get("/get_parent_of_cell")
def get_parent_of_cell(cell, res: int = None):
    return h3.cell_to_parent(cell, res)


@router.get("/get_children_of_cell")
def get_children_of_cell(cell, res: int = None):
    return h3.cell_to_children(cell, res)


@router.get("/get_cell_to_center_child")
def get_cell_to_center_child(cell,res: int = None):
    return h3.cell_to_center_child(cell, res)


@router.get("/get_cell_to_children_size")
def get_cell_to_children_size(cell, res: int = None):
    return h3.cell_to_children_size(cell, res)


@router.get("/get_cell_to_child_pos")
def get_cell_to_child_pos(child, res_parent: int):
    return h3.cell_to_child_pos(child, res_parent)


@router.get("/get_child_pos_to_cell")
def get_child_pos_to_cell(child, res_parent: int, child_pos: int):
    return h3.child_pos_to_cell(child, res_parent, child_pos)