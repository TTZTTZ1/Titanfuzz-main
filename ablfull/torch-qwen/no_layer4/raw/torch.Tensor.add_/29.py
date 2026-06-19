import torch

# Prepare valid input data
a = torch.tensor([1.0, 2.0], dtype=torch.float)
other = torch.tensor([3.0, 4.0], dtype=torch.float)
alpha = 2.0

# Call the API
result = a.add_(other, alpha=alpha)

print(result)