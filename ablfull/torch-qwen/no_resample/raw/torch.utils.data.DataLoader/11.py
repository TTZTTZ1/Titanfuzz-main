import torch
from torch.utils.data import DataLoader

# Create a simple dataset
dataset = torch.randn(10, 3, 224, 224)

# Prepare valid input data
batch_size = 2
shuffle = False
num_workers = 0
pin_memory = False
drop_last = False

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers, pin_memory=pin_memory, drop_last=drop_last)