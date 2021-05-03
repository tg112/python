import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, title="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinate in [[38.2, -99.1], [37.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinate, popup="Hi i am a marker", icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("./Map.html")