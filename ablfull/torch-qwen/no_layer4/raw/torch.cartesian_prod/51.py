import torch

# Prepare input data
tensor1 = torch.tensor([1, 2])
tensor2 = torch.tensor([0.5, 0.7])

# Call the API
result = torch.cartesian_prod(tensor1, tensor2)

print(result)