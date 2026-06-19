import torch

# Prepare valid input data
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])

# Call the API
result = torch.cartesian_prod(x, y)

print(result)