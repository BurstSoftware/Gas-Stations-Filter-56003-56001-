import streamlit as st
import pandas as pd

# Data for gas stations
data = [
    {"type": "Kwik Trip", "address": "1740 Commerce Drive, North Mankato, MN, 56003", "town": "North Mankato", "zip": "56003", "lat": 44.1795484, "lon": -94.0366175},
    {"type": "Kwik Trip", "address": "1701 Monks Ave, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.1465, "lon": -94.001},  # Approximate
    {"type": "Kwik Trip", "address": "17 Stoltzman Rd, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.159626, "lon": -94.01457},
    {"type": "Kwik Trip", "address": "1549 Madison Ave, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.1663483, "lon": -93.9646679},
    {"type": "Kwik Trip", "address": "921 Coneflower Lane, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.155, "lon": -93.961},  # Approximate
    {"type": "Kwik Trip", "address": "1291 Raintree Road, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.1779152, "lon": -93.9675506},
    {"type": "Kwik Trip", "address": "1271 Riverfront Drive, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.188128, "lon": -94.0130452},
    {"type": "Kwik Trip", "address": "1701 Premier Dr, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.173, "lon": -93.956},  # Approximate
    {"type": "Casey's General Store", "address": "1375 Lookout Drive, North Mankato, MN", "town": "North Mankato", "zip": "56003", "lat": 44.1683231, "lon": -94.0467194},
    {"type": "Casey's General Store", "address": "2001 Riverfront Drive, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.185, "lon": -94.009},  # Approximate
    {"type": "Casey's General Store", "address": "170 St Andrews Drive, Mankato, MN", "town": "Mankato", "zip": "56001", "lat": 44.172, "lon": -93.96},  # Approximate
    {"type": "Casey's General Store", "address": "101 598th Ave, Eagle Lake, MN", "town": "Eagle Lake", "zip": "56024", "lat": 44.1698662, "lon": -93.8934832},
]

df = pd.DataFrame(data)

st.title("Gas Station Finder")

# Filters
station_type = st.selectbox("Select Gas Station Type", ["All"] + list(df["type"].unique()))
town = st.selectbox("Select Town", ["All"] + list(df["town"].unique()))
zip_code = st.selectbox("Select Zip Code", ["All"] + list(df["zip"].unique()))

# Filter the dataframe
filtered_df = df.copy()
if station_type != "All":
    filtered_df = filtered_df[filtered_df["type"] == station_type]
if town != "All":
    filtered_df = filtered_df[filtered_df["town"] == town]
if zip_code != "All":
    filtered_df = filtered_df[filtered_df["zip"] == zip_code]

# Display filtered choices
st.subheader("Filtered Gas Stations")
st.dataframe(filtered_df[["type", "address", "town", "zip"]])

# Display map if not empty
if not filtered_df.empty:
    st.subheader("Locations on Map")
    map_df = filtered_df[["lat", "lon"]].rename(columns={"lat": "latitude", "lon": "longitude"})
    st.map(map_df)
else:
    st.write("No gas stations match the filters.")
