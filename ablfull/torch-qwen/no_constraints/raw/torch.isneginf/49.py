import torch

# Generate input data
x = -torch.inf

# Call the API
result = torch.isneginf(x)

print(result)