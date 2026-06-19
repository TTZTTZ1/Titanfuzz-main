import torch

# Prepare input data
a = torch.tensor([1.0, 2.0], dtype=torch.float)
other = torch.tensor([3.0, 4.0], dtype=torch.float)

# Call the API
a.add_(other, alpha=2.0)