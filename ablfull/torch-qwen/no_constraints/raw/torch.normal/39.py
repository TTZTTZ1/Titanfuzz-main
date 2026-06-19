import torch

# Generate input data
mean = torch.tensor([0.0])
std = torch.tensor([1.0])

# Call the API
result = torch.normal(mean, std)