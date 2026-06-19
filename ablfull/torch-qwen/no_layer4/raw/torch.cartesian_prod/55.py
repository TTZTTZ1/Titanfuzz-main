import torch

# Generate input data
tensor1 = torch.tensor([1, 2, 3], dtype=torch.int)
tensor2 = torch.tensor([4, 5], dtype=torch.float)

# Call the API
result = torch.cartesian_prod(tensor1, tensor2)

print(result)