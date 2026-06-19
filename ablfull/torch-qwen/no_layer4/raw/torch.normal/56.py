import torch

# Prepare valid input data
mean = torch.tensor([1.0, 2.0])
std = torch.tensor([0.5, 0.5])

# Call the API
result = torch.normal(mean=mean, std=std)