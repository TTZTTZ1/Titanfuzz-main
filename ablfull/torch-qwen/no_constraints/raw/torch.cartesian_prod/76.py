import torch

# Generate two tensors
tensor1 = torch.tensor([1, 2])
tensor2 = torch.tensor([3, 4])

# Call the torch.cartesian_prod function
result = torch.cartesian_prod(tensor1, tensor2)