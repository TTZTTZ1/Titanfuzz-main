import torch

# Prepare valid input data
x = torch.tensor([1.0, 2.0], dtype=torch.float32)
y = torch.tensor([1.5, 2.5], dtype=torch.float32)

# Call the API
result = x.nextafter(y)