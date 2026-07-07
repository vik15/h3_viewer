from fastapi import APIRouter
import h3

router = APIRouter(prefix="/edges")


@router.get("/cells_to_dir_edges")
def cells_to_dir_edges(origin, destination):
    return h3.cells_to_directed_edge(origin, destination)


@router.get("/dir_edge_to_cells")
def dir_edge_to_cells(edge):
    return h3.directed_edge_to_cells(edge)


@router.get("/get_dir_edge_origin")
def get_dir_edge_origin(edge):
    return h3.get_directed_edge_origin(edge)


@router.get("/get_dir_edge_dest")
def get_dir_edge_dest(edge):
    return h3.get_directed_edge_destination(edge)


@router.get("/origin_to_dir_edges")
def origin_to_dir_edges(origin):
    return h3.origin_to_directed_edges(origin)
