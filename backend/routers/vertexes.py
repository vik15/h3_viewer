from fastapi import APIRouter
import h3

router = APIRouter(prefix="/vertex")



@router.get("/cell_to_vertex")
def cell_to_vertex(cell, vertex_num: int):
    return h3.cell_to_vertex(cell, vertex_num)



@router.get("/cell_to_vertexes")
def cell_to_vertexes(cell):
    return h3.cell_to_vertexes(cell)



@router.get("/vertex_to_latlng")
def vertex_to_latlng(vertex):
    lat, long = h3.vertex_to_latlng(vertex)
    return f"{lat}, {long}"