import torch

# Prepare input data
a = torch.tensor([1.0, 2.0])
b = torch.tensor([3.0, 4.0])

# Call the API
a.add_(b)