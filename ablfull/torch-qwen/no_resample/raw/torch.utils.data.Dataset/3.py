import torch

# Create a simple dataset class inheriting from torch.utils.data.Dataset
class SimpleDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Instantiate the dataset
dataset = SimpleDataset()