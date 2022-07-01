"""
Script to download images from NASA Worldview
"""
import urllib.request
import datetime
from calendar import monthrange
import fire
import os


def download_MODIS_imgs(year_range, months, save_path, lon_range, lat_range,
                  deg2pix=100, satellite='Aqua', exist_skip=False, var='CorrectedReflectance',filetype='jpeg'):
    os.makedirs(save_path, exist_ok=True)

    lon1 = lon_range[0]; lon2 = lon_range[1]
    lat1 = lat_range[0]; lat2 = lat_range[1]
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    loc= (f'&extent={lon1},{lat1},{lon2},{lat2}')
    loc_str = f'_{lon1}-{lon2}_{lat1}-{lat2}'
    size = (f'&width={int(dlon * deg2pix)}&height={int(dlat * deg2pix)}')
    layer = (f'&layers=MODIS_{satellite}_{var},Coastlines')

    for yr in range(year_range[0], year_range[1]):
        for m in months:
            nday = monthrange(yr,m)[1]
            for nd in range(1,nday+1):
                date = datetime.datetime(yr, m, nd)
                d = str(date.strftime('%j'))
                print(date.strftime('%y %m %d'))
                url = ('https://gibs.earthdata.nasa.gov/image-download?TIME='+
                       str(yr)+d+loc+'&epsg=4326'+layer+
                       '&opacities=1,1&worldfile=false&format=image/'+filetype+
                       size)
                save_str = (save_path+f'/{satellite}_'+var+str(yr)+
                    date.strftime('%m')+'{:02d}'.format(date.day)+loc_str+
                    '.'+filetype)
                if exist_skip and os.path.exists(save_str):
                    print('Skip')
                else:
                    try:
                        urllib.request.urlretrieve(url, save_str)
                    except:
                        print(f'Download failed for {save_str}')


def download_imgs(year_range, months, save_path, lon_range, lat_range,
                  deg2pix=100, satellite='Aqua', exist_skip=False):
    os.makedirs(save_path, exist_ok=True)

    lon1 = lon_range[0]; lon2 = lon_range[1]
    lat1 = lat_range[0]; lat2 = lat_range[1]
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    loc= (f'&BBOX={lat1},{lon1},{lat2},{lon2}')
    loc_str = f'_{lon1}-{lon2}_{lat1}-{lat2}'
    size = (f'&WIDTH={int(dlon * deg2pix)}&HEIGHT={int(dlat * deg2pix)}')
    layer = (f'&LAYERS=MODIS_{satellite}_CorrectedReflectance_TrueColor,Coastlines')

    for yr in range(year_range[0], year_range[1]):
        for m in months:
            nday = monthrange(yr,m)[1]
            for nd in range(1,nday+1):
                date = datetime.datetime(yr, m, nd)
                d = str(date.strftime('%j'))
                # print(satellite + ' ' + date.strftime('%y %m %d') + ' ' + str(lon_range))
                url = ('https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME=' +
                       str(date.strftime('%Y-%m-%d')) + loc + '&CRS=EPSG:4326' + layer + '&FORMAT=image/jpeg' + size)
                print(url)
                save_str = (save_path+f'/{satellite}_CorrectedReflectance'+str(yr)+
                    date.strftime('%m')+'{:02d}'.format(date.day)+loc_str+
                    '.jpeg')
                if exist_skip and os.path.exists(save_str):
                    print('Skip')
                else:
                    try:
                        urllib.request.urlretrieve(url, save_str)
                    except:
                        print(f'Download failed for {save_str}')
                #break


if __name__ == '__main__':
    fire.Fire(download_imgs)
