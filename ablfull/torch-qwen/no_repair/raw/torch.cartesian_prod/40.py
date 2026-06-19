import torch

# Prepare valid input data
t1 = torch.tensor([1, 2], dtype=torch.int)
t2 = torch.tensor([3, 4], dtype=torch.float)

# Call the API
result = torch.cartesian_prod(t1, t2)

print(result)