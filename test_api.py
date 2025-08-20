#!/usr/bin/env python3
"""
Simple test script for Myanmar Dam API
Tests the key endpoints to ensure they return expected data structure
"""

import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8000"

def test_endpoint(endpoint: str, expected_keys: list) -> bool:
    """Test an API endpoint and verify it returns expected keys"""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}")
        if response.status_code != 200:
            print(f"❌ {endpoint} failed with status {response.status_code}")
            return False
        
        data = response.json()
        missing_keys = [key for key in expected_keys if key not in data]
        if missing_keys:
            print(f"❌ {endpoint} missing keys: {missing_keys}")
            return False
        
        print(f"✅ {endpoint} - OK")
        return True
    except Exception as e:
        print(f"❌ {endpoint} error: {e}")
        return False

def main():
    """Run API tests"""
    print("🧪 Testing Myanmar Dam API endpoints...")
    print("=" * 50)
    
    # Test basic endpoints
    tests = [
        ("/", ["message"]),
        ("/api/dams/map", ["total_dams", "region_filter", "dams"]),
        ("/api/regions", ["total_regions", "regions"]),
        ("/api/stats", ["total_dams", "total_capacity_mcm", "main_uses"]),
    ]
    
    passed = 0
    total = len(tests)
    
    for endpoint, expected_keys in tests:
        if test_endpoint(endpoint, expected_keys):
            passed += 1
    
    # Test specific dam data structure
    print("\n🔍 Testing dam data structure...")
    try:
        response = requests.get(f"{BASE_URL}/api/dams/map")
        data = response.json()
        
        if data["total_dams"] > 0:
            dam = data["dams"][0]
            required_dam_keys = ["id", "name", "coordinates", "water_info", "details"]
            missing = [key for key in required_dam_keys if key not in dam]
            if missing:
                print(f"❌ Dam structure missing keys: {missing}")
            else:
                print("✅ Dam data structure - OK")
                
                # Check coordinate structure
                coords = dam["coordinates"]
                if "latitude" in coords and "longitude" in coords:
                    print("✅ Coordinates structure - OK")
                else:
                    print("❌ Coordinates missing lat/lon")
                
                # Check water info structure  
                water_info = dam["water_info"]
                water_keys = ["capacity_mcm", "area_sqkm", "depth_m", "elevation_masl"]
                missing_water = [key for key in water_keys if key not in water_info]
                if missing_water:
                    print(f"❌ Water info missing: {missing_water}")
                else:
                    print("✅ Water info structure - OK")
    except Exception as e:
        print(f"❌ Dam structure test error: {e}")
    
    # Test region filtering
    print("\n🔍 Testing region filtering...")
    try:
        response = requests.get(f"{BASE_URL}/api/dams/map?region=Sagaing")
        data = response.json()
        
        if data["region_filter"] == "Sagaing" and data["total_dams"] > 0:
            print("✅ Region filtering - OK")
        else:
            print("❌ Region filtering failed")
    except Exception as e:
        print(f"❌ Region filtering test error: {e}")
    
    print("=" * 50)
    print(f"📊 Results: {passed}/{total} endpoint tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Myanmar Dam API is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the API implementation.")

if __name__ == "__main__":
    main()