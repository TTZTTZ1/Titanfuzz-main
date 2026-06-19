import torch

# Prepare valid input data
tensors = [torch.tensor([1, 2]), torch.tensor([3, 4])]

# Call the API
result = torch.cartesian_prod(*tensors)

print(result)