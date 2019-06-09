import folium
print(dir(folium))
#create a map object
map = folium.Map(location=[20.462521, 85.882988], zoom_start = 7,tiles = 'cuttack')
print(map)

print(dir(folium.Map))
print(map.save('test.html'))

map2 = folium.Map(location=[20.462521, 85.882988], zoom_start = 15,tiles = 'bhubaneswar')
print(map2)
print(map2.save('test2.html'))
