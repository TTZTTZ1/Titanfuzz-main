import torch

# Prepare input data
x = torch.tensor([-1.0, -2.0, 3.0], dtype=torch.float32)
y = torch.tensor([1.0, -1.0, -1.0], dtype=torch.float32)

# Call the API
result = x.copysign_(y)