import torch

# Prepare input data
x = torch.tensor([1.0], dtype=torch.float32)
y = 1.5

# Call the API
result = x.nextafter_(y)