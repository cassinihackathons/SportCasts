from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib



def combine_data(dataset, dataweights, lon, lat, time, title, cmap):
    time_iteration = 0
    for time_hr in time:
        weighted_sum = np.zeros((len(lat), len(lon)))
        for data, weight in zip(dataset, dataweights):
            array = np.array(data[time_iteration][0])
            weighted_array = np.multiply(array, weight)
            weighted_sum = weighted_array + weighted_sum
        time_iteration+=1
        plt.imshow(weighted_sum, interpolation='gaussian', cmap=cmap, extent=[min(lon), max(lon), min(lat), max(lat)])
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title(title.format(time_hr))
        plt.savefig(('./images/{}.png').format(title.format(time_hr)))




nc_file = './data/ENS_FORECAST_2021-06-19.nc'
data = Dataset(nc_file, mode='r')
lon = data.variables['longitude'][:]
lat = data.variables['latitude'][:]
time = data.variables['time'][:]

mpg_conc = data.variables['mpg_conc'][:]
apg_conc = data.variables['apg_conc'][:]
bpg_conc = data.variables['bpg_conc'][:]
gpg_conc = data.variables['gpg_conc'][:]
opg_conc = data.variables['opg_conc'][:]
rwpg_conc = data.variables['rwpg_conc'][:]
dust = data.variables['dust'][:]
nmvoc_conc = data.variables['nmvoc_conc'][:]
o3_conc = data.variables['o3_conc'][:]
pm10_conc = data.variables['pm10_conc'][:]



pollen_data_weights = [1, 1, 1, 1, 1, 1]
pollen_dataset = [mpg_conc, apg_conc, bpg_conc, gpg_conc, opg_conc, rwpg_conc, dust, nmvoc_conc, o3_conc, pm10_conc]
pollen_set_name = ['mpg_conc', 'apg_conc', 'bpg_conc', 'gpg_conc', 'opg_conc', 'rwpg_conc']

combine_data(pollen_dataset, pollen_data_weights, lon, lat, time, 'Pollen concentration at T={}', 'inferno')


pollutants_data_weights = [1, 1, 1, 1]
pollutants_dataset = [dust, nmvoc_conc, o3_conc, pm10_conc]
pollutants_set_name = ['dust', 'nmvoc_conc', 'o3_conc', 'pm10_conc']

combine_data(pollutants_dataset, pollutants_data_weights, lon, lat, time, 'Pollutant concentration at T={}', matplotlib.colors.LinearSegmentedColormap.from_list("", ["green", "yellow", "red"]))
