import torch

# Generate input data
mean = torch.tensor(0.0)
std = torch.tensor(1.0)
size = (3, 3)

# Call the API
output = torch.normal(mean, std, size)

print(output)