from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from geo_utils import load_dams, load_barriers, get_dam_map_data
import json

app = FastAPI(
    title="Myanmar Dam Map API",
    description="API for Myanmar dam and reservoir data with coordinates and water level information",
    version="1.0.0"
)

# Add CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Myanmar Dam Map API"}

@app.get("/api/dams/map")
def get_dams_for_map(region: str = Query(None, description="Filter dams by admin unit (region/state)")):
    """Get dam data optimized for map display with coordinates and water level info"""
    try:
        dam_data = get_dam_map_data(region)
        return dam_data
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/api/dams")
def get_dams(region: str = Query(None, description="Filter dams by admin unit (region/state)")):
    """Get complete dam data in GeoJSON format"""
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

@app.get("/api/regions")
def get_available_regions():
    """Get list of available admin units (regions/states) for filtering"""
    try:
        dams = load_dams()
        regions = sorted(dams["ADMIN_UNIT"].dropna().unique().tolist())
        return {
            "total_regions": len(regions),
            "regions": regions
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/api/stats")
def get_dam_statistics():
    """Get overall statistics about Myanmar dams"""
    try:
        dams = load_dams()
        total_capacity = float(dams["CAP_MCM"].sum())
        total_area = float(dams["AREA_SKM"].sum())
        avg_depth = float(dams["DEPTH_M"].mean())
        
        # Convert pandas Series to plain Python dict with proper types
        main_uses_counts = dams["MAIN_USE"].value_counts()
        main_uses_dict = {str(k): int(v) for k, v in main_uses_counts.items()}
        
        stats = {
            "total_dams": len(dams),
            "total_capacity_mcm": round(total_capacity, 2),
            "total_area_sqkm": round(total_area, 2),
            "average_depth_m": round(avg_depth, 2),
            "main_uses": main_uses_dict,
            "construction_years": {
                "earliest": int(dams["YEAR_DAM"].min()) if not dams["YEAR_DAM"].isna().all() else None,
                "latest": int(dams["YEAR_DAM"].max()) if not dams["YEAR_DAM"].isna().all() else None
            }
        }
        return stats
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
