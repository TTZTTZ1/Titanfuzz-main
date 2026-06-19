import torch

# Generate input data
x = torch.tensor([2.0])

# Call the API
result = torch.special.psi(x)

print(result)