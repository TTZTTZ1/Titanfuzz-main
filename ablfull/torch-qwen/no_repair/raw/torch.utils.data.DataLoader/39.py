import torch

# Prepare valid input data
dataset = torch.tensor([1, 2, 3, 4, 5])
batch_size = 2
shuffle = False
num_workers = 0

# Call the API
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, num_workers=num_workers)