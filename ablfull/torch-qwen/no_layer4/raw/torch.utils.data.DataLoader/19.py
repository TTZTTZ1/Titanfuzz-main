import torch
from torch.utils.data import DataLoader

# Create a dummy dataset
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))

# Initialize DataLoader
dataloader = DataLoader(dataset, batch_size=2, shuffle=False)