import torch

# Generate valid input data
x = torch.tensor([1.0], dtype=torch.float32)
y = torch.tensor(2.0, dtype=torch.float32)

# Call the target API
result = x.nextafter_(y)