import geopandas as gpd
import warnings
warnings.filterwarnings('ignore', module='pyogrio')

def load_dams(region=None, gdb_path="data/gdb/GDW_v1_0.gdb", layer="GDW_reservoirs_v1_0"):
    gdf = gpd.read_file(gdb_path, layer=layer, driver="OpenFileGDB")
    myanmar_gdf = gdf[gdf["COUNTRY"] == "Myanmar"].to_crs("EPSG:4326")
    if region:
        myanmar_gdf = myanmar_gdf[myanmar_gdf["ADMIN_UNIT"].str.contains(region, case=False, na=False)]
    return myanmar_gdf

def get_dam_map_data(region=None):
    """Get dam data formatted for map display with coordinates and water level info"""
    dams_gdf = load_dams(region)
    
    dam_features = []
    for idx, dam in dams_gdf.iterrows():
        # Get centroid coordinates for point display on map
        centroid = dam.geometry.centroid
        
        feature = {
            "id": dam.get("GDW_ID", idx),
            "name": dam.get("DAM_NAME", "Unknown"),
            "reservoir_name": dam.get("RES_NAME", ""),
            "coordinates": {
                "longitude": centroid.x,
                "latitude": centroid.y
            },
            "water_info": {
                "capacity_mcm": dam.get("CAP_MCM", 0),  # Million cubic meters
                "area_sqkm": dam.get("AREA_SKM", 0),     # Square kilometers 
                "depth_m": dam.get("DEPTH_M", 0),        # Meters
                "elevation_masl": dam.get("ELEV_MASL", 0) # Meters above sea level
            },
            "details": {
                "river": dam.get("RIVER", ""),
                "main_use": dam.get("MAIN_USE", ""),
                "year_built": dam.get("YEAR_DAM", ""),
                "admin_unit": dam.get("ADMIN_UNIT", ""),
                "dam_height_m": dam.get("DAM_HGT_M", 0),
                "dam_length_m": dam.get("DAM_LEN_M", 0)
            }
        }
        dam_features.append(feature)
    
    return {
        "total_dams": len(dam_features),
        "region_filter": region,
        "dams": dam_features
    }

def load_barriers(region=None, gdb_path="data/gdb/GDW_v1_0.gdb", layer="GDW_barriers_v1_0"):
    gdf = gpd.read_file(gdb_path, layer=layer, driver="OpenFileGDB")
    myanmar_gdf = gdf[gdf["COUNTRY"] == "Myanmar"].to_crs("EPSG:4326")
    if region:
        myanmar_gdf = myanmar_gdf[myanmar_gdf["ADMIN_UNIT"].str.contains(region, case=False, na=False)]
    return myanmar_gdf

