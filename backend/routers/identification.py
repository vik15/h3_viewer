from fastapi import APIRouter
import h3

router = APIRouter(prefix="/identify")


@router.get("/is_valid_cell")
def is_valid_cell(cell):
    return h3.is_valid_cell(cell)


@router.get("/is_pentagon")
def is_pentagon(cell):
    return h3.is_pentagon(cell)


@router.get("/is_res_class_III")
def is_res_class_III(cell):
    return h3.is_res_class_III(cell)


@router.get("/is_valid_directed_edge")
def is_valid_directed_edge(edge):
    return h3.is_valid_directed_edge(edge)


@router.get("/is_valid_vertex")
def is_valid_vertex(vertex):
    return h3.is_valid_vertex(vertex)


@router.get("/is_valid_index")
def is_valid_index(cell):
    return is_valid_index(cell)