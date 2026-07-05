import h3
import requests
from fastapi import FastAPI, HTTPException
from haversine import haversine, Unit
from enum import Enum
from pydantic import BaseModel

app = FastAPI()


class AreaUnit(str, Enum):
    M2 = "m^2"
    KM2 = "km^2"


class DistanceUnit(str, Enum):
    M = "m"
    KM = "km"
    MI = "mi"
    FT = "ft"
    IN = "in"


class CellsShape(BaseModel):
    cells : list[str]
    tight : bool = True



@app.get("/")
def root():
    return "H3 viewer FastAPI App"


## latlong to h3index
@app.get("/latlong_to_cell")
def latlong_to_cell(lat: float,long: float, res: int = 9):
    return h3.latlng_to_cell(float(lat), float(long), res)


## get centroid(latlng) of a cell
@app.get("/get_centroid_of_cell")
def get_centroid_of_cell(cell):
    lat , long = h3.cell_to_latlng(cell)
    return f"{lat}, {long}"


## area of cell(s)
@app.get("/get_area_of_cells")
def get_area_of_cells(cells,unit: AreaUnit):
    return h3.cell_area(cells,unit)


# distance between 2 h3index
@app.get("/calculate_distance")
def distance_of_h3(cell1, cell2, unit : DistanceUnit):
    pt1 = h3.cell_to_latlng(cell1)
    pt2 = h3.cell_to_latlng(cell2)

    return haversine(pt1, pt2,unit)


## Get neighbouring h3 cells
@app.get("/get_neighbouring_cells")
def get_neighbouring_cells(cell, k: int =1):
    return h3.grid_ring(cell,k)


@app.get("/get_grid_distance")
def get_grid_distance(cell1, cell2):
    try:
        return h3.grid_distance(cell1, cell2)
    except Exception as e:
        raise HTTPException(
        status_code=400, 
        detail="Unable to compute H3 grid distance. The cells may be too far apart or invalid.",
        )


@app.get("/get_cell_boundaries")
def get_cell_boundaries(cell):
    return h3.cell_to_boundary(cell)



@app.post("/get_cells_h3_shape")
def get_cells_h3_shape(cell: CellsShape):
    h3_shape = h3.cells_to_h3shape(cell.cells,tight=cell.tight)
    return h3_shape
