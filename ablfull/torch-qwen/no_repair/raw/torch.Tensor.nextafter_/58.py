import torch

# Prepare input data
a = torch.tensor([1.0], dtype=torch.float32)
b = torch.tensor([2.0], dtype=torch.float32)

# Call the API
result = torch.Tensor.nextafter_(a, b)
print(result)