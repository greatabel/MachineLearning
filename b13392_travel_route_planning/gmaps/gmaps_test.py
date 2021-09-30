from os import environ


import gmaps
import gmaps.datasets

password = environ.get('GOOGLE_API_KEY')

gmaps.configure(api_key=password) # Fill in with your API key

earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
earthquake_df.head()

locations = earthquake_df[['latitude', 'longitude']]
weights = earthquake_df['magnitude']
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))

