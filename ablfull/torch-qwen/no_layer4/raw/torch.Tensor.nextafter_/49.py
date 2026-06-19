import torch

# Prepare valid input data
a = torch.tensor([1.0], dtype=torch.float32)
b = torch.tensor([2.0], dtype=torch.float32)

# Call the target API
result = torch.Tensor.nextafter_(a, b)