import torch

# Generate input data
x = torch.tensor([-1.5, -0.4, 0.3, 1.7])

# Call the API
result = torch.special.round(x)

print(result)