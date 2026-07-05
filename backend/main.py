import h3
import requests
from fastapi import FastAPI, HTTPException
from typing import Literal
from haversine import haversine, Unit
from enum import Enum
from pydantic import BaseModel

from routers import index_repr, identification, geo_coordinates, cell_grid_rel, conversion_func, hierarchical_rel, cell_properties


app = FastAPI()

@app.get("/", tags=['Home'])
def root():
    return "H3 viewer FastAPI App"


app.include_router(identification.router, tags=['Identification'])
app.include_router(index_repr.router, tags=['Index representaion'])
app.include_router(cell_properties.router, tags=['Cell properties'])
app.include_router(geo_coordinates.router, tags=['Geographic coordinates'])
app.include_router(hierarchical_rel.router, tags=['Hierarchical relationships'])
app.include_router(cell_grid_rel.router, tags=['Cell grid relationships'])
app.include_router(conversion_func.router, tags=['Conversion functions'])


