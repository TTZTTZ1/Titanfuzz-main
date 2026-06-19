import torch

# Generate input data
tensor1 = torch.tensor([1, 2], dtype=torch.int)
tensor2 = torch.tensor([3, 4], dtype=torch.float)

# Call the API
result = torch.cartesian_prod(tensor1, tensor2)
print(result)