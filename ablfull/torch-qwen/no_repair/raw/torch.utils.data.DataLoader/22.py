import torch
from torch.utils.data import DataLoader, TensorDataset

# Create a simple dataset
data = torch.randn(10, 3)
dataset = TensorDataset(data)

# Initialize DataLoader
dataloader = DataLoader(dataset, batch_size=2, shuffle=False)

# Iterate through the dataloader to trigger the call
for batch in dataloader:
    print(batch)