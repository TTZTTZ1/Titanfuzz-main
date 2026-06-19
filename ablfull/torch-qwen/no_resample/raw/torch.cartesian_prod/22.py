import torch

# Generate valid input data
a = torch.tensor([1, 2], dtype=torch.int)
b = torch.tensor([3, 4], dtype=torch.float)

# Call the API
result = torch.cartesian_prod(a, b)
print(result)