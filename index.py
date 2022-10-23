import folium
import pandas as pd
map = folium.Map(location=[28,0],starting_zoom=5)
tooltip = "Click me!"
folium.Marker(
    [28, 0], popup="<i>ADRAR</i>",
     tooltip=tooltip,
     icon=folium.Icon(icon="cloud")
).add_to(map)
folium.Circle(
    radius=500,
    location=[27.89085, -0.28656],
    
    popup="adrar univ",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(map)
map.add_child(folium.LatLngPopup())
url = (
    "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
)
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(map)









map.save("map.html")