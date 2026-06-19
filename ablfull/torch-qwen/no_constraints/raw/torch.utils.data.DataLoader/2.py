import torch
from torch.utils.data import DataLoader

# Prepare valid input data
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))
batch_size = 4
shuffle = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)