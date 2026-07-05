import h3
import requests
from fastapi import FastAPI, HTTPException
from typing import Literal
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
    """Convert Latitude, Longitude to a Cell"""
    return h3.latlng_to_cell(float(lat), float(long), res)


## get centroid(latlng) of a cell
@app.get("/get_centroid_of_cell")
def get_centroid_of_cell(cell):
    """Convert a Cell to Latitude, Longitude (Centroid)"""
    lat , long = h3.cell_to_latlng(cell)
    return f"{lat}, {long}"



@app.get("/get_str_to_int")
def get_str_to_int(cell):
    return h3.str_to_int(cell)



@app.get("/get_int_to_str")
def get_int_to_str(cell):
    return h3.int_to_str(cell)



@app.get("/get_parent_of_cell")
def get_parent_of_cell(cell):
    return h3.cell_to_parent(cell)



@app.get("/get_children_of_cell")
def get_children_of_cell(cell):
    return h3.cell_to_children(cell)


## area of cell(s)
@app.get("/get_area_of_cells")
def get_area_of_cells(cells,unit: AreaUnit):
    """Calculate area of selected cell(s)"""
    return h3.cell_area(cells,unit)


# distance between 2 h3index
@app.get("/calculate_distance")
def distance_of_h3(cell1: str, cell2: str , unit : DistanceUnit):
    """Calculate distance between two cells"""
    pt1 = h3.cell_to_latlng(cell1)
    pt2 = h3.cell_to_latlng(cell2)

    return h3.great_circle_distance(pt1, pt2,unit)



@app.get("/distance_bw_latlng")
def distance_bw_latlng(
    lat1: float, lng1: float, lat2: float, lng2: float,
    unit: Literal["m", "km"] = "m"):
    """Calculate distance between two latlng"""

    p1 = (lat1,lng1)
    p2 = (lat2,lng2)
    return h3.great_circle_distance(p1, p2 , unit)


## Get neighbouring h3 cells
@app.get("/get_neighbouring_cells")
def get_neighbouring_cells(cell, k: int =1, disk : bool = True):
    """Get Neighbouring Cells of a cell"""
    if disk:
        return h3.grid_disk(cell, k)
    else: 
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



@app.get("/get_grid_path_cells")
def get_grid_path_cells(cell1, cell2):
    return h3.grid_path_cells(cell1, cell2)



@app.get("/get_cell_boundaries")
def get_cell_boundaries(cell):
    return h3.cell_to_boundary(cell)



@app.post("/get_cells_h3_shape")
def get_cells_h3_shape(cell: CellsShape):
    h3_shape = h3.cells_to_h3shape(cell.cells,tight=cell.tight)
    return h3_shape



@app.get("/get_resolution")
def get_resolution(cell):
    return h3.get_resolution(cell)



@app.get("/get_base_cell_number")
def get_base_cell_number(cell):
    return h3.get_base_cell_number(cell)



@app.get("/get_all_pentagons")
def get_all_pentagons(res=9):
    return h3.get_pentagons(res)



@app.get("/is_pentagon")
def is_pentagon(cell):
    return h3.is_pentagon(cell)
