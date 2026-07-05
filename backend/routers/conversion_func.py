from fastapi import APIRouter
from pydantic import BaseModel
import h3

router = APIRouter(prefix="/convert")



class CellsShape(BaseModel):
    cells : list[str]
    tight : bool = True


@router.post("/get_cells_h3_shape")
def get_cells_h3_shape(cell: CellsShape):
    h3_shape = h3.cells_to_h3shape(cell.cells,tight=cell.tight)
    return h3_shape
