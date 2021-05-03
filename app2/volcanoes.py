import pandas as pd
import folium

data = pd.read_csv("./volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def produceColor(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 2000:
        return "orange"
    else:
        return "red"


html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[38.58, -99.09], zoom_start=6, title="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(
        folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(iframe),
            icon=folium.Icon(produceColor(el)),
        )
    )

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open("./world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            "fillColor": "yellow"
            if x["properties"]["POP2005"] < 10000000
            else "orange"
            if 80000000 <= x["properties"]["POP2005"]
            else "red"
        },
    )
)

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("./Volcanoe.html")
