import torch
from torch.utils.data import Dataset

# Create a simple dataset subclass
class SimpleDataset(Dataset):
    def __init__(self, data):
        self.data = data
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx]

# Prepare valid input data
data = [1, 2, 3, 4, 5]
dataset = SimpleDataset(data)

# Call the API
print(len(dataset))