import torch
from torch.utils.data import Dataset

# Task 2: Generate input data
class MyDataset(Dataset):
    def __init__(self):
        # Example data
        self.data = [1, 2, 3, 4, 5]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Task 3: Call the API
dataset = MyDataset()