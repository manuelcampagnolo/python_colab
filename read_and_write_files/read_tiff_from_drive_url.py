! pip install rasterio
import rasterio
from rasterio.plot import show
import gdown

def url_to_id(url):
    x = url.split("/")
    return x[5]

# url of tif file from google drive
url='https://drive.google.com/file/d/1-3JEkN3hH3huXEnC9kE7Yqlk6KpsqGIX/view?usp=sharing' 
file_id=url_to_id(url) # '1-3JEkN3hH3huXEnC9kE7Yqlk6KpsqGIX'
url_1="https://drive.google.com/uc?id={}".format(file_id)
print(url_id)

# saves local copy of tif file
output = 'image.tif'
gdown.download(url_id, output, quiet=False)

# open local file
img = rasterio.open(output)
show(img)
