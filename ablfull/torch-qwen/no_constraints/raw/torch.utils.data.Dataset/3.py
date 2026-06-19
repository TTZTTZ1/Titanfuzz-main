import torch
from torch.utils.data import Dataset

# Create a simple dataset class inheriting from Dataset
class SimpleDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]

# Prepare valid input data
data = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]

# Call the API
dataset = SimpleDataset(data)