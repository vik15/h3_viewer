from fastapi import APIRouter
from typing import Literal
from enum import Enum
import h3

router = APIRouter(prefix="/coordinates")

class DistanceUnit(str, Enum):
    M = "m"
    KM = "km"
    RD = "rads"

class AreaUnit(str, Enum):
    M2 = "m^2"
    KM2 = "km^2"
    RD2 = "rads^2"


@router.get("/latlong_to_cell")
def latlong_to_cell(lat: float,long: float, res: int = 9):
    """Convert Latitude, Longitude to a Cell"""
    return h3.latlng_to_cell(float(lat), float(long), res)


@router.get("/get_centroid_of_cell")
def get_centroid_of_cell(cell):
    """Convert a Cell to Latitude, Longitude (Centroid)"""
    lat , long = h3.cell_to_latlng(cell)
    return f"{lat}, {long}"


@router.get("/get_area_of_cells")
def get_area_of_cells(cells,unit: AreaUnit = AreaUnit.KM2):
    """Calculate area of selected cell(s)"""
    return h3.cell_area(cells,unit)



@router.get("/get_cell_boundaries")
def get_cell_boundaries(cell):
    return h3.cell_to_boundary(cell)


@router.get("/dir_edge_to_bndry")
def dir_edge_to_bndry(edge):
    return h3.directed_edge_to_boundary(edge)


@router.get("/calculate_distance")
def distance_of_h3(cell1: str, cell2: str , unit : DistanceUnit = DistanceUnit.KM):
    """Calculate distance between two cells"""
    pt1 = h3.cell_to_latlng(cell1)
    pt2 = h3.cell_to_latlng(cell2)

    return h3.great_circle_distance(pt1, pt2, unit)


@router.get("/distance_bw_latlng")
def distance_bw_latlng(
    lat1: float, lng1: float, lat2: float, lng2: float,
    unit: DistanceUnit = DistanceUnit.KM):
    """Calculate distance between two latlng"""

    p1 = (lat1,lng1)
    p2 = (lat2,lng2)
    return h3.great_circle_distance(p1, p2 , unit)


@router.get("/avg_hex_area")
def avg_hex_area(res: int, unit: AreaUnit = AreaUnit.KM2):
    return h3.average_hexagon_area(res,unit)


@router.get("/avg_hex_edge_len")
def avg_hex_edge_len(res: int, unit: DistanceUnit = DistanceUnit.KM):
    return h3.average_hexagon_edge_length(res,unit)
