import torch

# Prepare valid input data
x = torch.tensor([1.0, 2.0], dtype=torch.float)
y = torch.tensor([3.0, 4.0], dtype=torch.float)

# Call the API
x.add_(y, alpha=2.0)