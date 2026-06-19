import torch

# Prepare valid input data
tensor1 = torch.tensor([1, 2])
tensor2 = torch.tensor([3, 4])

# Call the target API
result = torch.cartesian_prod(tensor1, tensor2)