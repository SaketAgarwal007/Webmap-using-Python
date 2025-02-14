import folium
import pandas as pd
data = pd.read_csv("Volcanoes.txt")
lat =list(data["LAT"])
lon =list(data["LON"])
elev =list(data["ELEV"])  #ELEV is from volcanoes.txt file.
name =list(data["NAME"])
html = """Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>  
Height: %s m
"""  #Here a href is used to anchor the google link.
def color_producer(elevation):
    if elevation <1000:
        return "green"
    elif 1000<= elevation <3000:
        return "orange"
    else:
        return "Red"
map = folium.Map(location=[38.58, -99.01], zoom_start=5, tiles="Stamen Terrain")

fg= folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, name in zip(lat, lon ,elev, name):
    iframe = folium.IFrame(html=html % (name+" Volcano", name+" Volcano", el), width=200, height=100)
    fg.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),fill_color=color_producer(el), fill_opacity=0.7, color="grey"))
pg =folium.FeatureGroup(name="Population data")
pg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
style_function=lambda x:{"fillColor":"green" if x["properties"]["POP2005"] < 10000000 
else "orange" if 10000000 <=x["properties"]["POP2005"] <20000000 else "red"}))  #Here fillColor is to be written this way only,
map.add_child(fg)
map.add_child(pg)
map.add_child(folium.LayerControl())
map.save("Map.html")