import torch

# Prepare input data
tensors = [torch.tensor([1, 2], dtype=torch.int), torch.tensor([0.5, 0.75], dtype=torch.float)]

# Call the API
result = torch.cartesian_prod(*tensors)

print(result)