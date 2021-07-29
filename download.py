import os
import shutil
import urllib.request
from tqdm import tqdm

URL = "https://ndownloader.figshare.com/articles/1512427/versions/5"
FILE_NAME = "mri_example.zip"

# Download File

print('Downloading File ...')

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, output_path):
    with DownloadProgressBar(unit='B', unit_scale=True,
                                miniters=1, desc=output_path) as t:
        urllib.request.urlretrieve(url, filename=output_path, reporthook=t.update_to)

# download_url(URL, FILE_NAME)

print('Extracting Zip File ...')
shutil.unpack_archive(FILE_NAME, FILE_NAME.split(".")[0])

extracting_dir = f"{FILE_NAME.split('.')[0]}"
inner_file_list = os.listdir(extracting_dir)
for file in inner_file_list:
    if file.split(".")[-1].lower() == "zip":
        zip_path = os.path.join(extracting_dir, file)
        data_path = os.path.join(extracting_dir, "data")
        shutil.unpack_archive(zip_path, data_path)