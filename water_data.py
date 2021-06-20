from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt


def make_plt(VHM0, lon, lat, X, Y, dx, dy, time_iter):

    plt.imshow(np.flip(VHM0, (0)), vmin=0, vmax=1,extent=[min(lon), max(lon), min(lat), max(lat)])
    plt.quiver(X, Y, dx, dy, color='black', scale=35, width=0.002)
    plt.title('Wave height and dir at T={}'.format(3 * time_iter))
    plt.savefig(('./images/Wave height and dir at T={}.jpg'.format(3 * time_iter)))
    plt.delaxes()

nc_file = './data/global-analysis-forecast-wav-001-027_1624138927603.nc'
data = Dataset(nc_file, mode='r')
lon = data.variables['longitude'][:]
lat = data.variables['latitude'][:]
time = data.variables['time'][:]
var_names = ['VHM0','VMDR']

time_iter = 0
for x in time:
    VHM0 = np.array(data.variables['VHM0'][time_iter])
    dx = np.cos(np.array(data.variables['VMDR'][time_iter]))
    dx[np.where(dx==0.9822633)]=0
    dy = np.sin(np.array(data.variables['VMDR'][time_iter]))
    dy[np.where(dy==-0.18750656)]=0
    X, Y = np.meshgrid(lon,lat)
    make_plt(VHM0, lon, lat, X, Y, dx, dy, time_iter)
    time_iter+=1


