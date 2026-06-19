import torch

# Prepare valid input data
tensors = [torch.tensor([1, 2], dtype=torch.int), torch.tensor([3, 4], dtype=torch.float)]

# Call the target API
result = torch.cartesian_prod(*tensors)
print(result)