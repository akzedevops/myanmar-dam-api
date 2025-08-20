# Myanmar Dam Map API 🏞️

A comprehensive FastAPI application that provides detailed information about Myanmar's dams and reservoirs, including coordinates, water levels, capacity, and other vital statistics for mapping and analysis purposes.

## Features ✨

- **92 Myanmar dams** with comprehensive data
- **Water level information** including capacity, surface area, depth, and elevation
- **Precise coordinates** (latitude/longitude) for each dam
- **Regional filtering** by Myanmar's administrative units
- **Map-friendly API** optimized for interactive mapping applications
- **Statistical summaries** of dam data
- **Interactive demo** with visual map display

## API Endpoints 🛠️

### 🗺️ `/api/dams/map` - Map-Optimized Dam Data
Returns dam data formatted for interactive maps with coordinates and water information.

**Query Parameters:**
- `region` (optional): Filter dams by admin unit (region/state)

**Response Example:**
```json
{
  "total_dams": 92,
  "region_filter": null,
  "dams": [
    {
      "id": 329,
      "name": "Thaphanseik",
      "coordinates": {
        "longitude": 95.37099681111906,
        "latitude": 23.41928255315838
      },
      "water_info": {
        "capacity_mcm": 3550.0,
        "area_sqkm": 332.1,
        "depth_m": 10.7,
        "elevation_masl": 143
      },
      "details": {
        "river": "Mu",
        "main_use": "Irrigation",
        "year_built": 2001,
        "admin_unit": "Sagaing",
        "dam_height_m": 33,
        "dam_length_m": 6885
      }
    }
  ]
}
```

### 🏢 `/api/regions` - Available Regions
Get list of available administrative units for filtering.

### 📊 `/api/stats` - Dam Statistics
Get overall statistics about Myanmar's dams.

**Response Example:**
```json
{
  "total_dams": 92,
  "total_capacity_mcm": 23161.9,
  "total_area_sqkm": 1372.72,
  "average_depth_m": 19.54,
  "main_uses": {
    "": 74,
    "Irrigation": 13,
    "Hydroelectricity": 4,
    "Water supply": 1
  },
  "construction_years": {
    "earliest": 1950,
    "latest": 2016
  }
}
```

### 🗺️ `/api/dams` - Complete GeoJSON Data
Returns complete dam data in GeoJSON format with full geometries.

### 🚧 `/api/barriers` - Barrier Data
Returns barrier/obstacle data in GeoJSON format.

## Installation & Setup 🚀

1. **Clone the repository:**
   ```bash
   git clone https://github.com/akzedevops/myanmar-dam-api.git
   cd myanmar-dam-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API server:**
   ```bash
   python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. **Open the interactive demo:**
   - Open `demo.html` in your web browser
   - Or visit: `http://localhost:8000/docs` for API documentation

## Testing 🧪

Run the test suite:
```bash
python test_api.py
```

## Data Sources 📊

The API uses the Global Dam Watch (GDW) dataset containing:
- **Dam locations** with precise coordinates
- **Water capacity** in million cubic meters (MCM)
- **Surface area** in square kilometers
- **Water depth** and elevation data
- **Construction details** and usage information
- **Administrative boundaries** for filtering

## Key Data Fields 📋

### Water Information
- **capacity_mcm**: Water storage capacity in million cubic meters
- **area_sqkm**: Surface area in square kilometers  
- **depth_m**: Average depth in meters
- **elevation_masl**: Elevation in meters above sea level

### Dam Details
- **dam_height_m**: Physical dam height in meters
- **dam_length_m**: Dam length in meters
- **river**: River name where dam is located
- **main_use**: Primary purpose (Irrigation, Hydroelectricity, etc.)
- **year_built**: Construction year
- **admin_unit**: Administrative region/state

## Interactive Demo 🎮

The `demo.html` file provides a complete interactive map showing:
- ✅ All Myanmar dams plotted on an interactive map
- ✅ Detailed popup information for each dam
- ✅ Water level and capacity information
- ✅ Regional filtering functionality
- ✅ Statistical summaries
- ✅ Responsive design for different screen sizes

![API Demo Screenshot](demo_screenshot.png)

## Regional Coverage 🌏

The API covers dams across Myanmar's administrative units including:
- Sagaing, Mandalay, Magway
- Bago, Yangon, Ayeyarwady  
- Shan, Kachin, Kayah
- Chin, Kayin, Mon, Rakhine
- Tanintharyi

## API Documentation 📚

Visit `http://localhost:8000/docs` when the server is running to explore the interactive API documentation with:
- Complete endpoint descriptions
- Request/response examples
- Parameter documentation
- Try-it-now functionality

## Development 👨‍💻

Built with:
- **FastAPI** - Modern Python web framework
- **GeoPandas** - Geospatial data processing
- **Leaflet** - Interactive mapping (demo)
- **OpenStreetMap** - Base map tiles

## Contributing 🤝

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Made with ❤️ for Myanmar's water resource management and development community**