import torch

# Prepare input data
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6]])

# Call the API
result = torch.cartesian_prod(tensor1, tensor2)

print(result)