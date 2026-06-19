import torch

# Create a simple dataset
class SimpleDataset(torch.utils.data.Dataset):
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