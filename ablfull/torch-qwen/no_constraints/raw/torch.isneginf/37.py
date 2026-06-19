import torch

# Generate input data
x = -float('inf')

# Call the API
result = torch.isneginf(x)
print(result)