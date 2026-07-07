from fastapi import APIRouter
import h3


router = APIRouter()


@router.get("/get_icosahedron_faces")
def get_icosahedron_faces(cell):
    return h3.get_icosahedron_faces(cell)


@router.get("/cell_to_local_ij")
def cell_to_local_ij(origin, cell):
    return h3.cell_to_local_ij(origin, cell)


@router.get("/local_ij_to_cell")
def local_ij_to_cell(origin, i: int, j: int):
    return h3.local_ij_to_cell(origin, i, j)