import torch

# Generate input data
x = torch.tensor([0.0], dtype=torch.float32)
y = torch.tensor([1.0], dtype=torch.float32)

# Call the API
result = x.nextafter(y)