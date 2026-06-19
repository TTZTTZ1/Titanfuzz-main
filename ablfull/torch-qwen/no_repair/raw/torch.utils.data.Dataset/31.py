import torch
from torch.utils.data import Dataset

# Create a subclass of Dataset
class MyDataset(Dataset):
    def __init__(self):
        # Example data
        self.data = [1, 2, 3, 4, 5]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Instantiate the dataset
dataset = MyDataset()

# Print the dataset to verify it works
print(dataset)