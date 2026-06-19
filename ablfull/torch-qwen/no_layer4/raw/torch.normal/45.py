import torch

# Prepare input data
mean = torch.tensor([0.5])
std = torch.tensor([0.5])

# Call the API
result = torch.normal(mean=mean, std=std)