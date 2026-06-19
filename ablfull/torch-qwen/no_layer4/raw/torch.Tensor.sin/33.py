import torch

# Generate input data
x = torch.tensor([0.0, 1.0, 2.0], dtype=torch.float32)

# Call the API
result = x.sin()