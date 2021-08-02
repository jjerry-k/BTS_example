import h5py
import numpy as np
from torch.utils.data import Dataset, DataLoader

def load_mat(filepath):
    mat = h5py.File(filepath, "r")
    label = mat['cjdata']['label'].__array__()
    img = mat['cjdata']['image'].__array__()
    img = img/img.max()
    mask = mat['cjdata']['tumorMask'].__array__()
    mat.close()
    return img, label, mask

class MriDataset(Dataset):
    
    def __init__(self, root_dir):
        self.dir = root_dir
        self.file_list = [file for file in os.listdir(root_dir) if file.split(".")[-1] == "mat"]

    def __len__(self):
        return len(self.file_list)
    
    def __getitem__(self, idx):
        img, label, mask = load_mat(os.path.join(self.dir, self.file_list[idx]))
        return img[np.newaxis], label[0], mask

class MriLoader():
    def __init__(self):
        pass