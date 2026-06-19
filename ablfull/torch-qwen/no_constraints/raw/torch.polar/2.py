import torch

# Generate input data
r = torch.tensor([1.0])
theta = torch.tensor([0.5])

# Call the API
result = torch.polar(r, theta)