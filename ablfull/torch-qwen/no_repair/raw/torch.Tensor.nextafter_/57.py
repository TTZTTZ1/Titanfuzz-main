import torch

# Prepare input data
self_tensor = torch.tensor([1.0], dtype=torch.float32)
other_value = torch.tensor([1.000001], dtype=torch.float32)

# Call the API
result = torch.nextafter(self_tensor, other_value)