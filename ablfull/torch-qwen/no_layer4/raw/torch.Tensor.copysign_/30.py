import torch

# Generate input data
a = torch.tensor([-1.0, -2.0, 3.0], dtype=torch.float32)
b = torch.tensor([1.0, -1.0, -1.0], dtype=torch.float32)

# Call the API
a.copysign_(b)