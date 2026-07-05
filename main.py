import h3
import requests


def latlngtocell(lat,lng,res=9):
    return h3.latlng_to_cell(lat,lng,res)

# latitude = input("Input Latitude: ")

latitude = 18.99868402458938
longitude = 72.81605439750471
# 19.00961631822194, 72.83324956750482
print(latlngtocell(latitude,longitude))