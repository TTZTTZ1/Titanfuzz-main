import torch

# Prepare valid input data
a = torch.tensor([1, 2, 3], dtype=torch.long)
b = torch.tensor([4, 5], dtype=torch.float)

# Call the API
result = torch.cartesian_prod(a, b)
print(result)