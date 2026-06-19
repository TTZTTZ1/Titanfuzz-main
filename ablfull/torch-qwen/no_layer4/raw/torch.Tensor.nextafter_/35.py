import torch

# Generate input data
self_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)
other_value = torch.tensor([1.5, 2.5], dtype=torch.float32)

# Call the API
result = self_tensor.nextafter(other_value)