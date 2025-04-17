import geopandas as gpd

def load_dams(region=None, gdb_path="data/gdb/GDW_v1_0.gdb", layer="GDW_reservoirs_v1_0"):
    gdf = gpd.read_file(gdb_path, layer=layer, driver="OpenFileGDB")
    myanmar_gdf = gdf[gdf["COUNTRY"] == "Myanmar"].to_crs("EPSG:4326")
    if region:
        myanmar_gdf = myanmar_gdf[myanmar_gdf["ADMIN_UNIT"].str.contains(region, case=False, na=False)]
    return myanmar_gdf

def load_barriers(region=None, gdb_path="data/gdb/GDW_v1_0.gdb", layer="GDW_barriers_v1_0"):
    gdf = gpd.read_file(gdb_path, layer=layer, driver="OpenFileGDB")
    myanmar_gdf = gdf[gdf["COUNTRY"] == "Myanmar"].to_crs("EPSG:4326")
    if region:
        myanmar_gdf = myanmar_gdf[myanmar_gdf["ADMIN_UNIT"].str.contains(region, case=False, na=False)]
    return myanmar_gdf

