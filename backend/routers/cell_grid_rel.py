from fastapi import FastAPI, APIRouter, HTTPException
import h3


router = APIRouter(prefix="/grid")

## Get neighbouring h3 cells
@router.get("/get_neighbouring_cells")
def get_neighbouring_cells(cell, k: int =1, disk : bool = True):
    """Get Neighbouring Cells of a cell"""
    if disk:
        return h3.grid_disk(cell, k)
    else: 
        return h3.grid_ring(cell,k)



@router.get("/get_grid_distance")
def get_grid_distance(cell1, cell2):
    try:
        return h3.grid_distance(cell1, cell2)
    except Exception as e:
        raise HTTPException(
        status_code=400, 
        detail="Unable to compute H3 grid distance. The cells may be too far apart or invalid.",
        )



@router.get("/get_grid_path_cells")
def get_grid_path_cells(cell1, cell2):
    return h3.grid_path_cells(cell1, cell2)
