import torch

# Generate input data
tensors = [torch.tensor([1, 2, 3]), torch.tensor([4, 5])]

# Call the API
result = torch.cartesian_prod(*tensors)

print(result)