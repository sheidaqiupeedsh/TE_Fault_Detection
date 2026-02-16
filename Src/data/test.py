import json
import pandas as pd

# -----------------------
# File paths
# -----------------------
geojson_path = "C:/Users/Sheidaqiupeedsh/TE_Fault_Detection/Fault_detection_project/data/raw/BIPC_GIS.geojson"
excel_path = "C:/Users/Sheidaqiupeedsh/TE_Fault_Detection/Fault_detection_project/data/raw/Metering_SensorList.xlsx"
output_path = "C:/Users/Sheidaqiupeedsh/TE_Fault_Detection/Fault_detection_project/data/raw/plants_completed.geojson"

# -----------------------
# Load GeoJSON (ONLY for structure & coordinates)
# -----------------------
with open(geojson_path, "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

# Build a lookup: complex_name -> coordinates
coordinates_map = {}
for feature in geojson_data["features"]:
    cname = feature["properties"].get("complex_name", "").strip()
    coordinates_map[cname] = feature["geometry"]["coordinates"]

# -----------------------
# Load Excel (SOURCE OF TRUTH)
# -----------------------
df = pd.read_excel(excel_path)

# Clean text
df["complex_name"] = df["complex_name"].str.strip()
df["farsi_name"] = df["farsi_name"].str.strip()

# -----------------------
# Group Excel by complex_name
# -----------------------
grouped = df.groupby("complex_name", sort=False)

# -----------------------
# Build NEW GeoJSON
# -----------------------
new_features = []

for complex_name, group in grouped:
    if complex_name not in coordinates_map:
        print(f"⚠ No coordinates found for: {complex_name}")
        continue

    feature = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": coordinates_map[complex_name]
        },
        "properties": {
            "complex_name": complex_name,
            "farsi_name": group["farsi_name"].iloc[0],
            "fluid": group["fluid"].tolist(),     # one-to-one with tag_id
            "tag_id": group["tag_id"].tolist()    # ALL tag_ids preserved
        }
    }

    new_features.append(feature)

final_geojson = {
    "type": "FeatureCollection",
    "features": new_features
}

# -----------------------
# Save output
# -----------------------
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(final_geojson, f, ensure_ascii=False, indent=2)

print("✅ GeoJSON rebuilt strictly from Excel (structure preserved)")