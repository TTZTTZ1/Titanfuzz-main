import torch
from torch.utils.data import Dataset

class MyDataset(Dataset):

    def __init__(self):
        self.data = torch.randn(10, 5)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
dataset = MyDataset()
print(dataset[0])