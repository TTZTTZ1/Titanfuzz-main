import torch

# Prepare input data
self_tensor = torch.tensor([1.0], dtype=torch.float32)
other_value = 2.0

# Call the API
result = torch.Tensor.nextafter_(self_tensor, other_value)