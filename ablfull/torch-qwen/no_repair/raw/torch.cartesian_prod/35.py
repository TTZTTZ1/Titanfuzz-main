import torch

# Prepare valid input data
t1 = torch.tensor([1, 2, 3], dtype=torch.int)
t2 = torch.tensor([4.0, 5.0], dtype=torch.float)

# Call the API
result = torch.cartesian_prod(t1, t2)