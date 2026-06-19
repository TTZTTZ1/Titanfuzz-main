import torch

# Generate input data: x must be greater than or equal to 1
x = torch.tensor([2.0])

# Call the API
result = torch.arccosh(x)

print(result)