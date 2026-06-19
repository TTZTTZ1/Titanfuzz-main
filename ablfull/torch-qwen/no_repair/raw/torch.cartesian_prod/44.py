import torch

# Generate input data
tensors = [torch.tensor([1, 2]), torch.tensor([3, 4])]

# Call the API
result = torch.cartesian_prod(*tensors)