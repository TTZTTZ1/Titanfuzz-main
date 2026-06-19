import torch

# Prepare input data
a = torch.tensor([1.0, 2.0])
other = torch.tensor([3.0, 4.0])

# Call the API
result = a.add_(other)
print(result)