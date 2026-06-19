import torch

# Generate input data
x = torch.tensor([1.5, -2.3, 0.7])

# Call the API
result = torch.special.round(x)

print(result)