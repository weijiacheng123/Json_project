from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
import plotly
import json


outfile = open('US_fires_9_14.json', 'r')


infile = open('US_fires_9_14.json', 'r')
outfile = open('readable_US_fires_9_14.json', 'w')

eqdata = json.load(infile)
json.dump(eqdata, outfile, indent=4)

lats, lons, brit = [], [], []

for f in eqdata:
    if f['brightness'] > 450:
        lat = f['latitude']
        lon = f['longitude']
        lats.append(lat)
        lons.append(lon)
        bri = f['brightness']
        brit.append(bri)


print(lats[:5])
print(lons[:5])


#data = [Scattergeo(lon=lons, lat=lats)]

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.04*m for m in brit],
        'color':brit,
        'colorscale':'Viridis',
        'reversescale':True,
        'colorbar':{'title': 'Brightness'}
    }
}]


my_layout = Layout(title="US Fires - 9/14/2020 through 9/20/2020")

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename='USFires9.14.html')