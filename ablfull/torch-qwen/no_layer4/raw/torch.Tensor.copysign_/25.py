import torch

# Prepare valid input data
x = torch.tensor([-1.0, -2.0], dtype=torch.float32)
y = torch.tensor([1.0, 2.0], dtype=torch.float32)

# Call the API
x.copysign_(y)