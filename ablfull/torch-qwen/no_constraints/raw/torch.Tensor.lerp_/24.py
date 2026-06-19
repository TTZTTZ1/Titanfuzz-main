import torch

# Generate input data
a = torch.tensor([0.0, 1.0])
b = torch.tensor([4.0, 5.0])
weight = 0.5

# Call the API
result = a.lerp_(b, weight)
print(result)