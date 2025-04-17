from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from geo_utils import load_dams, load_barriers
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Myanmar Dam Map API"}

@app.get("/api/dams")
def get_dams(region: str = Query(None, description="Filter dams by admin unit (region/state)")):
    try:
        dams = load_dams(region)
        return JSONResponse(content=json.loads(dams.to_json()))
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/api/barriers")
def get_barriers(region: str = Query(None, description="Filter barriers by admin unit (region/state)")):
    try:
        barriers = load_barriers(region)
        return JSONResponse(content=json.loads(barriers.to_json()))
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
